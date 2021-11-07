from LoggingDecorator import logd

def test_print_message():
    @logd
    def function():
        return True