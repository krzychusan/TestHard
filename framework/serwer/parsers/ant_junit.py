import re

class AntJUnitParser:
   
    def __init__(self, input, name=''):
        self.log = input
        result = re.search('\[junit\] Tests run: (\d+), Failures: (\d+), Errors: (\d+), Time elapsed: ([^ ]+) sec', self.log)
        if not result:
            print 'Parse error in AntJUnitParser!'
            raise ValueException()

        vals = result.groups()
        self.tests_count = int(vals[0])
        self.failures = int(vals[1])
        self.errors = int(vals[2])
        self.time_elapsed = float(vals[3].replace(',', '.'))
        self.test_case_name = name

