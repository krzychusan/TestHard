
class BaseParser:

    def __init__(self, input):
        self.tests_count = 0
        self.failures = 0
        self.errors = 0
        self.time_elapsed = 0.0
        self.log = 'empty log'
