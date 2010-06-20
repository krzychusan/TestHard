from testhard.tests import *

class TestConfigureController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='configure', action='index'))
        # Test response...
