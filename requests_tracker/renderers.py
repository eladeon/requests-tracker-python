import json
import logging
import os
import shutil
from pathlib import Path

import jinja2
from urllib3.util import parse_url

from .request import RequestSessionContext
from .util import FileHelper

logger = logging.getLogger(__name__)


class Requests2HARRenderer:
    _sensitive_params: list
    _sensitive_values: list

    def __init__(self):
        pass

    def _safe_text_filter(self, txt_input: str):
        return json.dumps(txt_input, ensure_ascii=False)

    def _clean_param_value(self, param_name: str, param_value: str):
        output_str = param_value
        for sensitive_param in self._sensitive_params:
            if sensitive_param in param_name:
                output_str = param_value.replace(param_value, '*' * len(param_value))
                break
        return json.dumps(output_str, ensure_ascii=False)

    def _hide_sensitive_values(self, input_str: str):
        output_str = input_str
        for sensitive_var in self._sensitive_values:
            output_str = output_str.replace(sensitive_var, '*' * len(sensitive_var))
        return output_str

    def _rendering(
            self,
            request_session_context: RequestSessionContext,
            template_dir: str = Path(__file__).parent.joinpath('jinja'),
            template_name: str = 'req2har.jinja2'
    ):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
        env.filters['safe_text'] = self._safe_text_filter
        # env.filters['cast_int'] = self.cast_int
        env.globals['clean_param_value'] = self._clean_param_value
        template = env.get_template(template_name)
        logger.debug(f'Render HAR with template "{template.name}"')

        py = template.render(
            http_entries=request_session_context.entries
        )

        return py

    def exec(self, request_session_context: RequestSessionContext):
        self._sensitive_params = request_session_context.sensitive_params
        self._sensitive_values = request_session_context.sensitive_values

        logger.debug(f'Rendering Requests > HAR ...')

        rendered_text = self._rendering(request_session_context=request_session_context)

        logger.debug(f'Hiding sensitive variables ...')

        clean_text = self._hide_sensitive_values(rendered_text)

        return clean_text


class HAR2MarkdownRenderer:

    def __init__(self):
        pass

    def safe_text_filter(self, txt_input: str):
        """Custom filter"""
        return json.dumps(txt_input, ensure_ascii=False)

    def _load_entries(self, file_path: str):
        har_txt = FileHelper.read_file_contents(file_path)
        har_json = json.loads(har_txt)
        return har_json['log']['entries']

    def _filter_entries(self, all_entries: list, exclude_patterns: list) -> list:
        filtered_entries = []
        if len(exclude_patterns) == 0:
            filtered_entries = all_entries
        else:
            for entry in all_entries:
                request_url = str(entry['request']['url'])
                if any(ext in request_url for ext in exclude_patterns):
                    continue
                filtered_entries.append(entry)
        return filtered_entries

    def _prepare(self, http_entries: list):
        request_groups = {}

        for entry in http_entries:
            request_url = str(entry['request']['url'])
            entry['request']['clean_url'] = request_url.split('?')[0]
            parsed_url = parse_url(request_url)
            request_group = str(parsed_url.path)

            if request_group not in request_groups:
                request_groups[request_group] = 0

            request_groups[request_group] = request_groups[request_group] + 1
            request_id = f"{request_group}[{request_groups[request_group]}]"

            request_group_name_clean = str(parsed_url.path).replace('/', '_').replace('.', '_')
            content_file_name = f"{request_group_name_clean}_{request_groups[request_group]}.html"

            entry['request']['request_id'] = request_id
            entry['response']['content_file_name'] = content_file_name
            entry['response']['content_file_link'] = f"content/{content_file_name}"

    def _create_content_files(self, content_folder: str, http_entries: list):
        for entry in http_entries:
            content_file_path = Path.joinpath(Path(content_folder), entry['response']['content_file_name'])
            response_content = entry['response']['content'].get('text')
            if response_content is not None:
                FileHelper.write_file(str(content_file_path), response_content)
            elif entry['response']['content'].get('size') > 0 and int(entry['response']['status']) != 302:
                logger.warning(f"response content is missing for '{content_file_path}'")

    def _rendering(
            self,
            http_entries: list,
            template_dir: str = Path(__file__).parent.joinpath('jinja'),
            template_name: str = 'har2md.jinja2'
    ):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
        env.filters['safe_text'] = self.safe_text_filter
        template = env.get_template(template_name)
        logger.debug(f'Render HAR with template "{template.name}"')

        output_txt = template.render(
            http_entries=http_entries
        )

        return output_txt

    def exec(self, input_file: str, output_folder: str, exclude_patterns: list):

        if not os.path.exists(input_file):
            raise Exception(f"Invalid Input File Path '{input_file}' ")

        content_folder = str(Path.joinpath(Path(output_folder), 'content'))

        if Path(output_folder).exists():
            logger.debug(f"Deleting folder ({output_folder}) ...")
            shutil.rmtree(output_folder)

        logger.debug(f"Creating folder ({output_folder} ...")
        os.makedirs(output_folder)

        logger.debug(f"Creating folder ({content_folder} ...")
        os.makedirs(content_folder)

        all_entries = self._load_entries(input_file)
        filtered_entries = self._filter_entries(all_entries, exclude_patterns)
        self._prepare(filtered_entries)

        logger.debug(f"Filtered {len(all_entries)} entries down to {len(filtered_entries)} ...")

        logger.debug(f"Creating content files ...")
        self._create_content_files(content_folder, filtered_entries)

        renderer = HAR2MarkdownRenderer()
        rendered_txt = renderer._rendering(http_entries=filtered_entries)

        md_output_file = Path.joinpath(Path(output_folder), 'output.md')
        FileHelper.write_file(str(md_output_file), rendered_txt)
