"""
Module containing Logger object factory.
"""
from abc import ABCMeta, abstractmethod
from .logger import LoggerStream

class LoggerFactory(metaclass=ABCMeta): # pylint: disable = R0903
    """
    Abstract factory for Logger objects.
    """

    @abstractmethod
    def create_logger_stream(self, wrapped):
        """
        Abstract create_logger method.
        """

class Logger(LoggerFactory): # pylint: disable = R0903
    """
    Logger concrete factory (Concrete Factory).
    """
    def create_logger_stream(self, wrapped):
        """
        Method to return concrete CustomLogger object.
        """
        return LoggerStream(wrapped)
