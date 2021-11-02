"""
Module containing Logger object factory.
"""
from abc import ABCMeta, abstractmethod
from .custom_logger import CustomLogger

class LoggerFactory(metaclass=ABCMeta): # pylint: disable = R0903
    """
    Abstract factory for Logger objects.
    """

    @abstractmethod
    def create_logger(self):
        """
        Abstract create_logger method.
        """

# TODO fix factory...
class Logger(LoggerFactory): # pylint: disable = R0903
    """
    Logger concrete factory (Concrete Factory).
    """
    def create_logger(self):
        """
        Method to return concrete CustomLogger object.
        """
        return CustomLogger()
