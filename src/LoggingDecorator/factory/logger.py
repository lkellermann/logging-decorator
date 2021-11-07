"""
Module interface containing the types of Loggers.
"""
import logging
from .custom_logger import CustomLogger
from ..utils.shared_parameters import InnerParameters as ip
#  Wrap this class arround a decorator, so it will be easy to create new Logger types.

class LoggerStream(CustomLogger):
    """
    Class to build Log Streams to console (concrete product).
    """
    def __init__(self, wrapped):
        self.inner_parameters = ip()
        self.wrapped = wrapped
        self.logging = logging
        self.logger_handler = self.logging
        CustomLogger.__init__(self, self.logger_handler, logging, wrapped)

    @property
    def logger_handler(self):
        """
        logger_handler getter.
        """
        return self._logger_handler

    @property
    def inner_parameters(self):
        """
        inner_parameters getter.
        """
        return self._inner_parameters

    @property
    def wrapped(self):
        """
        wrapped getter.
        """
        return self._wrapped

    @logger_handler.setter
    def logger_handler(self, logging_object):
        """
        logger_handler setter.
        """
        handler = logging_object.StreamHandler()
        handler.setLevel(self.wrapped.logging_level)
        formatter = logging_object.Formatter(self.inner_parameters.logging_stream_format)
        handler.setFormatter(formatter)
        self._logger_handler = handler
        return self._logger_handler

    @inner_parameters.setter
    def inner_parameters(self, inner_parameter):
        self._inner_parameters = inner_parameter
        return self._inner_parameters

    @wrapped.setter
    def wrapped(self, _wrapped):
        """
        wrapped setter.
        """
        self._wrapped = _wrapped
        return self._wrapped
