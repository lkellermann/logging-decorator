"""
Main module to serve logd decorator.
"""
# pylint: disable=C0103
from .wrapped.logging import WrappedLoggingClass

def logd(*dargs, **dkwargs) -> object:
    """
    Decorator function that instantiates the LoggingDecorator object.

    Returns:
        object: the wrapped method result.
    """

    if (len(dargs) == 1 and callable(dargs[0])):

        def wrapper(original_method):
            def wrapped_function(*args, **kwargs):
                return WrappedLoggingClass()\
                    .call(original_method, *args, **kwargs)
            return wrapped_function
        return wrapper(dargs[0])


    def wrapper(original_method):   # pylint: disable=E0102
        def wrapped_function(*args, **kwargs):
            return WrappedLoggingClass(*dargs, **dkwargs)\
                .call(original_method, *args, **kwargs)
        return wrapped_function
    return wrapper
