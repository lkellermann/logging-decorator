"""
Module interface containing the types of Loggers.
"""
import logging
from .custom_logger import CustomLogger
from ..utils.shared_parameters import InnerParameters as ip
# TODO: Wrap this class arround a decorator, so it will be easy to create new Logger types.

class LoggerStream(CustomLogger):
    """
    Class to build Log Streams to console (concrete product).
    """
    def __init__(self, wrapped):
        super().__init__(self.logger_handler, logging, wrapped)

    @property
    def logger_handler(self):
        """
        logger_handler getter.
        """
        return self._logger_handler

    @logger_handler.setter
    def logger_handler(self):
        """
        logger_handler setter.
        """
        logger_handler = logging.StreamHandler()
        logger_handler.setLevel(ip.logging_level)
        logger_handler.setFormatter(ip.logging_stream_format)
        self._logger_handler = logger_handler
        return self._logger_handler
