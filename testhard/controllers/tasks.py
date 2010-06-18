import logging

from serwer.TasksManager import TasksManager

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TasksController(BaseController):

    def index(self):
        tm = TasksManager()
        c.tasks = tm.getTasks()
        return render('/tasks.mako')

    def showRaport(self):
        pass

