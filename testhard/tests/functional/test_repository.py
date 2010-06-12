from testhard.tests import *

class TestRepositoryController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='repository', action='index'))
        # Test response...
