"""
Module to extract method attributes and wrap it to generate logs.
"""
import logging
import inspect
from functools import lru_cache
from datetime import datetime
from ..utils.directory_manager import DirectoryManager

class WrappedLoggingClass: # pylint: disable=R0902
    """
    Class to wrap methods and get its attributes.
    """
    _debug_level={'critical':logging.CRITICAL,
                 'error':logging.ERROR,
                 'warning':logging.WARNING,
                 'info':logging.INFO,
                 'debug':logging.DEBUG,
                 'notset':logging.NOTSET
    }

    def __init__(self,
                 file:bool=False,
                 file_error_prefix: str = 'error',
                 raise_error:bool=True,
                 logging_level:str='debug'):
        """
        Object constructor.

        Args:
            file (bool, optional): write log message in a file if True. Defaults to False.
            raise_error (bool, optional): raise an error message and exit application if True.
                Defaults to True.
        """
        self.start_time = datetime.now()
        self.file = file
        self.original_method = None
        self.error_message = None
        self.method_variables = None
        self.method_name = None
        self.file_error_prefix = f'{file_error_prefix}_' if file_error_prefix is not None else ''
        self._raise_error = raise_error
        self.logging_level = logging_level
        if file:
            self.directory_manager = DirectoryManager(self.file_error_prefix)
            self.output_file = self.directory_manager
        else:
            self.directory_manager = None
            self.output_file = None




    def call(self, original_method: object, *args, **kwargs):
        """
        Method to run the original method and collect metadata to be logged.

        Args:
            original_method (object): generic method being wrapped.
        """
        # Update all properties depending on original_method.
        self.original_method = original_method

        if self.file:
            self.output_file = self.directory_manager
            print(f'OUTPUT FILE {self.output_file}')
        try:
            original_method(*args,**kwargs)
            self.error_message = None
        # The broad exception will generate the
        # LogException message to be logged.
        except Exception as exception:          # pylint: disable=broad-except
            self.error_message = str(exception)

        self.module_name = original_method
        self.method_name = original_method
        self.method_variables = original_method


    # Getters:
    @property
    def logging_level(self):
        """
        logging_level property getter.
        """
        return self._logging_level

    @property
    def original_method(self):
        """
        original_method property getter.
        """
        return self._original_method

    @property
    def method_variables(self):
        """
        method_variables property getter.
        """
        return self._method_variables

    @property
    def method_name(self):
        """
        method_name property getter.
        """
        return self._method_name

    @property
    def module_name(self):
        """
        module_name property getter.
        """
        return self._module_name

    @property
    def error_message(self):
        """
        error_message property getter.
        """
        return self._error_message

    @property
    def output_file(self):
        """
        output_file property getter.
        """
        return self._output_file


    # Setters
    @logging_level.setter
    def logging_level(self, debug_level):
        self._logging_level = WrappedLoggingClass._debug_level[debug_level]
        return self._logging_level

    @original_method.setter
    @lru_cache
    def original_method(self, original_method):
        """
        original_method property setter.
        """
        self._original_method = original_method
        return self._original_method

    @method_variables.setter
    def method_variables(self, original_method):
        """
        method_variables property setter.
        """
        if original_method is not None:
            self._method_variables = inspect.signature(original_method)
        else:
            self._method_variables = None
        return self._method_variables

    @method_name.setter
    def method_name(self, original_method):
        """
        method_name property setter.
        """
        if original_method is not None:
            self._method_name = original_method.__name__
        else:
            self._method_name = None

        return self._method_name

    @module_name.setter
    def module_name(self, original_method):
        """
        module_name property setter.
        """
        self._module_name =  original_method.__module__
        return self._module_name

    @error_message.setter
    def error_message(self, error_message):
        """
        error_message property setter.
        """
        self._error_message =  error_message
        return self._error_message

    @output_file.setter
    def output_file(self, dir_manager):
        """
        output_file property setter.
        """
        if self.file:
            self._output_file = dir_manager.output_file_path()
        else:
            self._output_file = None
        return self._output_file
