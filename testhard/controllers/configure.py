import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ConfigureController(BaseController):

    def index(self):
        return render('configure.mako')

    def doEdit(self):
        pass

