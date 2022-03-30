import logging
import os
from http.cookiejar import CookieJar, LWPCookieJar, Cookie
from os import path
from pathlib import Path

import requests

from .renderers import Requests2HARRenderer, HAR2MarkdownRenderer
from .request import RequestSessionContext

logger = logging.getLogger(__name__)
DEFAULT_SESSION_CACHE_FOLDER = 'session_cache'


class ICookieStorage:

    def load(self, session: requests.Session):
        pass

    def save(self, cookiejar: CookieJar):
        pass


class IRequestSessionStorage:

    def write(self, request_session_context: RequestSessionContext):
        pass

    def get_location(self) -> str:
        pass


class CookiesFileStorage(ICookieStorage):
    _cookies_file_path: Path

    def __init__(self, session_cache_path: Path, cookie_file_name: str = 'cookies.txt'):
        self._cookies_file_path = session_cache_path.joinpath(cookie_file_name)

    def load(self, session: requests.Session):
        file_path = self._cookies_file_path

        session_folder = self._cookies_file_path.parent
        if not path.exists(session_folder):
            logger.debug(f"creating folder '{session_folder}'...")
            os.makedirs(session_folder)

        if not path.exists(file_path):
            logger.debug(f"cookies file ('{file_path}') does not exist ...")
            return

        try:
            logger.debug(f"loading cookies from file ({file_path})...")

            lwp_cookiejar = LWPCookieJar()
            lwp_cookiejar.load(str(file_path), ignore_discard=True)
            for c in lwp_cookiejar:
                # noinspection PyTypeChecker
                args = dict(vars(c).items())
                args['rest'] = args['_rest']
                del args['_rest']
                c = Cookie(**args)
                session.cookies.set_cookie(c)

        except Exception as ex:
            logger.warning(f"could not load cookies from file ({file_path}): ({ex})")

    def save(self, cookiejar: CookieJar):
        file_path = self._cookies_file_path
        logger.debug(f"saving cookies to file ({file_path}) ...")

        lwp_cookiejar = LWPCookieJar()
        for c in cookiejar:
            # noinspection PyTypeChecker
            args = dict(vars(c).items())
            # noinspection PyUnresolvedReferences
            args['rest'] = args["_rest"]
            del args['_rest']
            c = Cookie(**args)
            lwp_cookiejar.set_cookie(c)

        lwp_cookiejar.save(str(file_path), ignore_discard=True, ignore_expires=True)


class RequestSessionFileStorage(IRequestSessionStorage):
    _requests_file_path: Path

    def __init__(self, requests_file_path):
        self._requests_file_path = requests_file_path

    def write(self, request_session_context: RequestSessionContext):
        session_folder = self._requests_file_path.parent
        if not path.exists(session_folder):
            logger.debug(f"creating folder '{session_folder}'...")
            os.makedirs(session_folder)

        har_output_json = Requests2HARRenderer().exec(request_session_context)

        logger.debug(f'saving file {self._requests_file_path}')

        with open(self._requests_file_path, 'w') as f:
            f.write(har_output_json)

    def get_location(self) -> str:
        return str(self._requests_file_path)


def create_local_cookie_storage(cookies_file: Path):
    return CookiesFileStorage(cookies_file)


def write_HAR_to_local_file(session_cache_path: Path, request_session_context: RequestSessionContext):
    dt_string = request_session_context.session_start_time.strftime("%d-%m-%Y %H-%M-%S")
    requests_file_path = session_cache_path.joinpath(f"session-{dt_string}.har")
    request_storage = RequestSessionFileStorage(requests_file_path=requests_file_path)
    request_storage.write(request_session_context)


def convert_HAR_to_markdown(session_cache_path: Path, request_session_context: RequestSessionContext):
    dt_string = request_session_context.session_start_time.strftime("%d-%m-%Y %H-%M-%S")
    requests_file_path = session_cache_path.joinpath(f"session-{dt_string}.har")

    input_file_path = requests_file_path
    output_folder_path = Path.joinpath(input_file_path.parent, input_file_path.stem)

    HAR2MarkdownRenderer().exec(
        input_file=str(input_file_path),
        output_folder=str(output_folder_path),
        exclude_patterns=[])
