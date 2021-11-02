"""
Module containing the LoggingDecorator package exceptions.
"""

class LogException(Exception):
    """
    Exception inherited from wrapped method.
    """
    def __init__(self, message): # pylint: disable= W0231
        self.message = message

    def __str__(self):
        return f'LogException[{self.message}]'
