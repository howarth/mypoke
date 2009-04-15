from poker.tests import *

class TestAjaxgameController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='ajaxgame', action='index'))
        # Test response...
