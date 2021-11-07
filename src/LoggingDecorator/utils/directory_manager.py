"""
Module to generate strings and create directories and files.
"""

from pathlib import PurePath, Path
from datetime import datetime
from typing import Union
from .shared_parameters import  DirectoryParameters

class DirectoryManager:
    """
    Class to create path strings, directories and files.
    """
    def __init__(self, file_error_prefix: Union[str, None]):
        self.file_error_prefix = file_error_prefix
        self.dir_param = DirectoryParameters
        self._create_log_folder()

    def _create_log_folder(self):
        """
        Method to create the log folder in working directory.
        """
        if Path(self.dir_param.log_folder).is_dir() is False:
            Path(self.dir_param.log_folder).mkdir(parents=True)

    def output_file_path(self):
        """
        Method to create output file path.
        """
        end = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'{self.file_error_prefix}{self.dir_param.cwd_name}_{end}'
        file_path = PurePath.joinpath(self.dir_param.log_folder, file_name)
        return file_path

    @staticmethod
    def write_output_log(file_path):
        """
        Method to write log file.
        """
        with open(file_path,'w',encoding='utf-8') as file:
            file.write()
        return file_path
