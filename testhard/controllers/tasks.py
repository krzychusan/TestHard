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

    def info(self):
        tm = TasksManager()
        c.name = request.params['name']
        return render('/tasksInfo.mako')
    
    def showRaport(self):
        tm = TasksManager()
        c.task = tm.getTask(request.params['name'])
        return render('/taskRaport.mako')

    def remove(self):
        tm = TasksManager()
        tm.removeTask(request.params['name'])
        c.link = '/tasks'
        c.message = 'Pomyslnie skasowano zadanie: ' + request.params['name']
        return render('message.mako')
