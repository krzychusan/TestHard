from testhard.tests import *

class TestTestsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='tests', action='index'))
        # Test response...
