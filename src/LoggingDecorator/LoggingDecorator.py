"""
Main module to serve logd decorator.
"""
# pylint: disable=C0103
from .wrapped.custom_logging import WrappedLoggingClass
from .wrapped import summary

def _create_client_summary(wrapped_object):
    streams = [summary.LoggerStreamSummary]
    for stream in streams:
        obj = stream(wrapped_object)
        obj.create_summary()
    return True

def logd(*dargs, **dkwargs) -> object:
    """
    Decorator function that instantiates the LoggingDecorator object.

    Returns:
        object: the wrapped method result.
    """

    if (len(dargs) == 1 and callable(dargs[0])):

        def wrapper(original_method):
            def wrapped_function(*args, **kwargs):
                wrapped_object = WrappedLoggingClass()
                _create_client_summary(wrapped_object)
                return wrapped_object\
                    .call(original_method, *args, **kwargs)
            return wrapped_function
        return wrapper(dargs[0])


    def wrapper(original_method):# pylint: disable=E0102
        def wrapped_function(*args, **kwargs):
            wrapped_object = WrappedLoggingClass(*dargs, **dkwargs)
            _create_client_summary(wrapped_object)
            return wrapped_object\
                .call(original_method, *args, **kwargs)
        return wrapped_function
    return wrapper
