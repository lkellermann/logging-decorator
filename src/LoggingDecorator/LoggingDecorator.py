################################################################################
# Filename: ./logging-decorator/src/LoggingDecorator.py                        #
# Path: /run/media/kellermann/files/git-repo/logging-decorator/src             #
# Created Date: Friday, August 27th 2021, 3:02:14 pm                           #
# Author: lkellermann                                                          #
#                                                                              #
# Copyright (c) 2021 Leandro Kellermann de Oliveira                            #
################################################################################
import logging
import inspect
from pathlib import Path, PurePath
from datetime import datetime

    
def logd(*dargs, **dkwargs) -> object:
    """Decorator function that instantiates the LoggingDecorator object.

    Returns:
        object: the wrapped method result.
    """

    if len(dargs) == 1 and callable(dargs[0]):
        
        def wrapper(original_method):
            def wrapped_function(*args, **kwargs):
                return LoggingDecorator().call(original_method, *args, **kwargs)    
            return wrapped_function    
        return wrapper(dargs[0])
    
    else:
        def wrapper(original_method):
            def wrapped_function(*args, **kwargs):
                return LoggingDecorator(*dargs, **dkwargs).call(original_method, *args, **kwargs)
            return wrapped_function
        return wrapper
    

class LoggingDecorator:
    debug_level={'critical':logging.CRITICAL,
                 'error':logging.ERROR,
                 'warning':logging.WARNING,
                 'info':logging.INFO,
                 'debug':logging.DEBUG,
                 'notset':logging.NOTSET        
    }
    
    def __init__(self,
                 file:bool=False,
                 raise_error:bool=True,
                 logging_level:str='debug'):
        """Object constructor.

        Args:
            file (bool, optional): write log message in a file if True. Defaults to False.
            raise_error (bool, optional): raise an error message and exit application if True. Defaults to True.
        """
        self._start_time = datetime.now()
        self._file = file
        self._raise_error = raise_error
        self._logging_level=LoggingDecorator.debug_level[logging_level]
        
        
    
    def call(self, original_method: object, *args, **kwargs):
        """Method to run the original method and collect metadata to be logged.

        Args:
            original_method (object): generic method being wrapped.
        """       
        try:
            original_method(*args,**kwargs)
            error_message = None
            args = None
            kwargs = None
        except Exception as e:
            error_message = str(e)
            
        return self._summary(original_method, 
                                         error_message,
                                         args,
                                         kwargs)
    
    
    def _summary(self,
                original_method:object,
                error_message:str=None,
                args:tuple=None,
                kwargs:dict=None) -> None:
        
        file = self._file
        raise_error = self._raise_error
        
        cwd = Path.cwd()
        cwd_name = cwd.name
        
        method_name = original_method.__name__
        module_name = original_method.__module__
        method_variables = inspect.signature(original_method)

        logging_level = self._logging_level
        logger = logging.getLogger(cwd_name)
        logger.handlers.clear()
        logger.setLevel(logging_level)

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        
        end_time = datetime.now()
        elapsed_time = end_time - self._start_time

        if file:
            # Create log folder if doesn't exist:
            log_folder = PurePath.joinpath(Path.cwd(),'log')
            if Path(log_folder).is_dir() == False:
                Path(log_folder).mkdir(parents=True)

            error_prefix = 'error_' if error_message is not None else ''
            
            output_log_name = f'{error_prefix}{cwd_name}_{method_name}_' + end_time.strftime('%d%b%Y_%H%M%S')
            output_log = PurePath.joinpath(log_folder, f'{output_log_name}.log')

            logger_file_handler = logging.FileHandler(output_log)
            logger_file_handler.setLevel(logging_level)
            logger_file_handler.setFormatter(formatter)
            logger.addHandler(logger_file_handler)
        else:
            output_log = None

        logger_console_handler = logging.StreamHandler()
        logger_console_handler.setLevel(logging_level)
        logger_console_handler.setFormatter(formatter)

        logger.addHandler(logger_console_handler)

        # Printing log info:
        logger.debug(f'Working directory:     {cwd}')
        logger.debug(f'Module name:           {module_name}')
        logger.debug(f'Method name:           {method_name}')
        logger.debug(f'Error message:         {error_message}')
        logger.debug(f'Start time:            {self._start_time}')
        logger.debug(f'End time:              {end_time}')
        logger.debug(f'Elapsed time:          {elapsed_time}')
        logger.debug(f'Variables:             {method_variables}')
        logger.debug(f'Args:                  {args}')
        logger.debug(f'Kwargs:                {kwargs}')
        logger.debug(f'Log path:              {output_log}')

        logging.shutdown()
        if raise_error == True and error_message is not None:
            raise LogException(error_message)

            
class LogException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f'LogException[{self.message}]'