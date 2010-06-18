import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

from serwer.TasksManager import TasksManager
from serwer.RepoManager import RepoManager
from serwer.IRepository import IRepository

log = logging.getLogger(__name__)

class RunController(BaseController):

    def index(self):
        con = RepoManager()
        c.repTypes = con.getRepositories()
        return render('/run.mako')
 
    def addRun(self):
        con = TasksManager()
        res = con.addTest(request.params['name'], request.params['repo'], 
                    request.params['date'], request.params['email'],
                    request.params['comment'])

        if res:
            c.message = 'Nowe zadanie %s dodane pomyslnie. ' % request.params['name']
            return render('/message.mako')
        else:
            c.message = 'Wystapil blad przy dodawaniu zadania %s. Sprobuj pozniej \
                        lub skontaktuj sie z administratorem.' % request.params['name']
            return render('/message.mako')
