from abc import ABCMeta, abstractmethod
from .custom_logging import WrappedLoggingClass
from ..factory import logger

class AbstractSummary(metaclass=ABCMeta):
    @abstractmethod
    def create_summary(self):
        pass


class LoggerStreamSummary:
    def __init__(self, wrapped: WrappedLoggingClass):
        self.wrapped = wrapped

    def create_summary(self):
        stream = logger.LoggerStream(self.wrapped)
        stream.output_logger()

class FileStreamSummary:
    pass