import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TestsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/tests.mako')
        # or, return a response
        return 'Hello World'
