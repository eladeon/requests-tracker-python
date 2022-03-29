from os import path
import logging
import sys
from pathlib import Path
from typing import Union


class LogHelper:
    @staticmethod
    def configure(log_level: Union[int, str]) -> logging.Logger:
        logger = logging.getLogger()
        logging.basicConfig()
        logger.setLevel(log_level)
        return logger

    @staticmethod
    def configure_std_out(log_level: int = 10) -> logging.Logger:
        logger = logging.getLogger()
        logging.basicConfig()
        logger.setLevel(log_level)
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        return logger


class FileHelper:
    @staticmethod
    def write_file(file_path: str, contents: str, mode='w') -> int:
        with open(file_path, mode=mode) as file:
            output = file.write(contents)
        return output

    @staticmethod
    def read_file_contents(file_path: str):
        if not path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist!")

        with open(file_path, mode='r') as file:
            contents = file.read()

        return contents


class DictionaryHelper:
    @staticmethod
    def merge_with_priority(higher_priority: dict, lower_priority: dict):
        result = lower_priority.copy()
        for key, val in higher_priority.items():
            result[key] = val
        return result


class PathHelper:
    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent
