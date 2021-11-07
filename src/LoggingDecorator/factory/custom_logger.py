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
        self.directory_parameters = dp()
        self.handler = handler
        self.logger = handler
        self.logging = logging

    @property
    def logger(self):
        """
        logger getter.
        """
        return self._logger

    @property
    def directory_parameters(self):
        """
        directory_parameters getter.
        """
        return self._directory_parameters

    @logger.setter
    def logger(self, handler_object):
        """
        logger setter.
        """
        cwd_name =  self.directory_parameters.cwd_name
        logger = self.logging.getLogger(cwd_name)
        logger.handlers.clear()
        logger.addHandler(handler_object)
        self._logger = logger
        return self._logger

    @directory_parameters.setter
    def directory_parameters(self, dp_object: dp):
        """
        directory_parameters setter.
        """
        self._directory_parameters = dp_object
        return self._directory_parameters

    def output_logger(self):
        end_time = datetime.now()
        elapsed_time = end_time - self.wrapped.start_time
        # print(f'{help(self.logger)}')
        # print(f'{self.logger.handle}')
        if self.logger.hasHandlers:
            # TODO get method attributes to log here:
            # print(f'PRINT - Working directory:     {self.directory_parameters.cwd}')
            self.logger.warning(f'Working directory:     {self.directory_parameters.cwd}')
            # self.logger.warning(f'Module name:           {self.wrapped.module_name}')
            # self.logger.warning(f'Method name:           {self.wrapped.method_name}')
            # self.logger.warning(f'Error message:         {self.wrapped.error_message}')
            # self.logger.warning(f'Start time:            {self.wrapped.start_time}')
            self.logger.warning(f'End time:              {end_time}')
            self.logger.warning(f'Elapsed time:          {elapsed_time}')
            # self.logger.debug(f'Variables:             {self.wrapped.method_variables}')
        else:
            raise ValueError('Logger has no handler attached.')
        if self.wrapped.file:
            self.logger.debug(f'Log path:              {self.wrapped.output_log}')

        self.logging.shutdown()
