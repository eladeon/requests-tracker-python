import argparse
import logging
from pathlib import Path

from .renderers import HAR2MarkdownRenderer
from .util import LogHelper

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'input',
        action='store',
        help='har input file',
    )

    parser.add_argument(
        '-e',
        '--exclude',
        action='store',
        default=None,
        type=str,
        help=(
            'CSV list of URL patterns to exclude'
        ),
    )

    parser.add_argument(
        '-o',
        '--output',
        action='store',
        default=None,
        type=str,
        help=(
            'output folder name'
        ),
    )

    parser.add_argument("--v", action="store_true",
                        help="Verbose (Log Level = DEBUG)")

    args = parser.parse_args()

    input_file_path = Path(args.input)

    exclude_pattern_csv = str(args.exclude).split(',')
    output_folder_path = Path.joinpath(input_file_path.parent, input_file_path.stem) \
        if args.output is None else args.output
    is_verbose = args.v

    LogHelper.configure(logging.DEBUG if is_verbose else logging.INFO)

    renderer = HAR2MarkdownRenderer()

    renderer.exec(
        input_file=str(input_file_path),
        output_folder=output_folder_path,
        exclude_patterns=exclude_pattern_csv)
