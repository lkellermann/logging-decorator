"""
Concrete CustomLogger factory module.
"""
from abc import ABCMeta, abstractmethod
from datetime import datetime
from ..utils.shared_parameters import DirectoryParameters as dp

class AbstractCustomLogger(metaclass=ABCMeta):  # pylint: disable=R0903
    """
    Abstract Custom Logger (Abstract Product).
    """
    @abstractmethod
    def output_logger(self):
        """
        Abstract method to output the log.
        """


class CustomLogger(AbstractCustomLogger):       # pylint: disable=R0903
    """
    CustomLogger Factory (Concrete factory).
    """

    def __init__(self, handler, logging, wrapped):
        self.wrapped = wrapped
        self.handler = handler
        self.logging = logging

    def output_logger(self):
        end_time = datetime.now()
        elapsed_time = end_time - self.wrapped.start_time
        self.handler.debug(f'Working directory:     {dp.cwd}')
        self.handler.debug(f'Module name:           {self.wrapped.module_name}')
        self.handler.debug(f'Method name:           {self.wrapped.method_name}')
        self.handler.debug(f'Error message:         {self.wrapped.error_message}')
        self.handler.debug(f'Start time:            {self.wrapped.start_time}')
        self.handler.debug(f'End time:              {end_time}')
        self.handler.debug(f'Elapsed time:          {elapsed_time}')
        self.handler.debug(f'Variables:             {self.wrapped.method_variables}')
        if self.wrapped.file:
            self.handler.debug(f'Log path:              {self.wrapped.output_log}')

        self.logging.shutdown()
