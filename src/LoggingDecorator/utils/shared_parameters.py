"""
Module containing dataclasses that will be used as parameters
among many modules.
"""
from dataclasses import dataclass
from pathlib import Path, PurePath

@dataclass(frozen=True)
class DirectoryParameters:
    """
    Directory constant parameters.
    Dynamically generated when the logd decorator is called.
    """
    cwd: Path = Path.cwd()
    cwd_name: str = cwd.name
    log_folder: PurePath = PurePath.joinpath(cwd, 'log')

@dataclass(frozen=False)
class InnerParameters:
    """
    Parameters provided by user and shared among many modules.
    logging_stream_format (str): possible values at  `https://docs.python.org/howto/logging.html`.
        Default is '%(asctime)s - %(message)s'.
    logging_level (str): 'critical', 'error', 'warning', 'info', 'debug', 'notset'.
        Default value is 'debug'.
    """
    logging_level: str = 'debug'
    logging_stream_format: str = '%(asctime)s - %(message)s'
    logging_file_format: str = '%(asctime)s - %(message)s'
