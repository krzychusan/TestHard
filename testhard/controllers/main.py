import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render
import common.dbutils as db
log = logging.getLogger(__name__)

class MainController(BaseController):

    def index(self):
        c.repCount = db.getCount('repositories')
        c.taskCount = db.getCount('tasks')
        return render('/main.mako')
