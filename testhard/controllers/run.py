import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

from serwer.RepoManager import RepoManager
from serwer.IRepository import IRepository

log = logging.getLogger(__name__)

class RunController(BaseController):

    def index(self):
        con = RepoManager()
        c.repTypes = con.getRepositories()
        return render('/run.mako')
    
