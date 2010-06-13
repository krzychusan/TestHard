import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

from framework.serwer.RepoManager import RepoManager
from framework.serwer.IRepository import IRepository

log = logging.getLogger(__name__)

class RepositoryController(BaseController):

    def index(self):
        # Return a rendered template
        con = RepoManager()
        c.repos = con.getRepositories()
        return render('/repository.mako')

    def add(self):
        con = RepoManager()
        c.repTypes = con.getRepositoriesTypes()
        c.repTypes = [it() for it in c.repTypes]
        return render('/repositoryAdd.mako')
    
    def doAdd(self):
        con = RepoManager()
        added = IRepository()
        #potrzeba sprawdzenia czy dane sa jako tako dobre i czy w ogole sa
        added.assign(request.params['name'], request.params['url'], request.params['comment'], request.params['type'])
        if request.params['login']:
            added.setAuth(request.params['login'], request.params['password'])
        added.setTestAttributes(request.params['build_cmd'], request.params['find_tests_cmd'], request.params['run_test_cmd'])
        con.addRepository(added)
        c.message = 'Pomyslnie dodano repozytorium %s ' % request.params['name']
        c.ret = '/repository'
        return render('/message.mako')

    def remove(self):
        return 'usuwam'
