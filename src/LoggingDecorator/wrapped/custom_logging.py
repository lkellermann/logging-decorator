"""
Module to extract method attributes and wrap it to generate logs.
"""
import logging
import inspect
from functools import lru_cache
from datetime import datetime

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
        self._file_error_prefix = f'{file_error_prefix}_' if file_error_prefix is not None else ''
        self._raise_error = raise_error
        self.logging_level = WrappedLoggingClass._debug_level[logging_level]



    def call(self, original_method: object, *args, **kwargs):
        """
        Method to run the original method and collect metadata to be logged.

        Args:
            original_method (object): generic method being wrapped.
        """
        try:
            self.original_method = original_method(*args,**kwargs)
            #self.method_variables = original_method
            #self.method_name= original_method
            self.module_name = original_method
            print(f'\n\n\nself.module_name: {self.module_name}\n\n\n')
            self.error_message = None
        # The broad exception will generate the
        # LogException message to be logged.
        except Exception as exception:          # pylint: disable=broad-except
            self.error_message = str(exception)

    # Getters:
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
        self._method_variables = inspect.signature(original_method)
        return self._method_variables

    @method_name.setter
    def method_name(self, original_method):
        """
        method_name property setter.
        """
        self._method_name = original_method.__name__
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
    def output_file(self, output_file):
        """
        output_file property setter.
        """
        self._output_file = output_file
        return self._output_file
