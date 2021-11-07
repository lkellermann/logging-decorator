"""
Module to generate strings and create directories and files.
"""

from pathlib import PurePath, Path
from datetime import datetime
from typing import Union
from .shared_parameters import  DirectoryParameters as dp

class DirectoryManager:
    """
    Class to create path strings, directories and files.
    """
    def __init__(self, file_error_prefix: Union[str, None]):
        self.file_error_prefix = file_error_prefix

    @staticmethod
    def create_log_folder():
        """
        Method to create the log folder in working directory.
        """
        if Path(dp.log_folder).is_dir() is False:
            Path(dp.log_folder).mkdir(parents=True)

    def output_file_path(self):
        """
        Method to create output file path.
        """
        end = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'{self.file_error_prefix}{dp.cwd_name}_{end}'
        file_path = PurePath.joinpath(dp.log_folder, file_name)
        return file_path

    def write_output_log(self):
        """
        Method to write log file.
        """
        file_path = self.output_file_path()
        with open(file_path,'w',encoding='utf-8') as file:
            file.write()
        return file_path
