import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

from framework.common.utils import setPath as sp
sp()

from serwer.RepoManager import RepoManager
from serwer.IRepository import IRepository

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
    
    def info(self):
        name = request.params['name']
        c.info = RepoManager().getRepository(name)
        return render('/repositoryInfo.mako')

    def doAdd(self):
        con = RepoManager()
        added = IRepository()
        #potrzeba sprawdzenia czy dane sa jako tako dobre i czy w ogole sa
        added.assign(request.params['name'], request.params['url'], request.params['comment'], request.params['type'])
        if request.params['login']:
            added.setAuth(request.params['login'], request.params['password'])
        added.setTestAttributes(request.params['build_cmd'], request.params['find_tests'], request.params['run_test'])
        if 'compile' in request.params and request.params['compile'] == 'on':
            added.compileOnServer = True
        con.addRepository(added)
        c.message = 'Pomyslnie dodano repozytorium %s ' % request.params['name']
        c.link = '/repository'
        return render('/message.mako')

    def remove(self):
        RepoManager().removeRepository(request.params['name'])
        c.link = '/repository'
        c.message = 'Pomyslnie skasowano repozytorium %s ' % request.params['name']
        return render('/message.mako')

    def edit(self):
        con = RepoManager()
        c.rep = con.getRepository(request.params['name'])
        c.repTypes = con.getRepositoriesTypes()
        c.repTypes = [it() for it in c.repTypes]
        return render('/repositoryEdit.mako')

    def doEdit(self):
        rep = IRepository()
        rep.assign(request.params['name'], request.params['url'], request.params['comment'], request.params['type'])
        if request.params['login']:
            rep.setAuth(request.params['login'], request.params['password'])
        rep.setTestAttributes(request.params['build_cmd'], request.params['find_tests'], request.params['run_test'])
        if 'compile' in request.params and request.params['compile'] == 'on':
            rep.compileOnServer = True
        if RepoManager().updateRepository(rep, request.params['old_name']):
            c.message = 'Pomyslnie edytowano repozytorium %s .' % request.params['old_name']
        else:
            c.message = 'Wystapil blad podczas edycji repozytorium %s. \
                Sprobuj ponownie pozniej, lub skontaktuj sie z administratorem.' % request.params['old_name']
        c.link = '/repository'
        return render('/message.mako')
