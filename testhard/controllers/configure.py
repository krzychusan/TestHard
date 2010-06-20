import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from testhard.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ConfigureController(BaseController):

    def index(self):
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read('./framework/serwer/config.txt')
        
        c.conf = {}
        c.conf['WorkerList'] = config.get('Worker', 'list')
        c.conf['WorkerPort'] = config.getint('Worker', 'port')
        c.conf['TmpFile'] = config.get('Rep', 'path')

        return render('configure.mako')

    def save(self):
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read('./framework/serwer/config.txt')
        config.set('Worker', 'list', request.params['WorkerList'])
        config.set('Worker', 'port', request.params['WorkerPort'])
        config.set('Rep', 'path', request.params['TmpFile'])
        with open('./framework/serwer/config.txt', 'wb') as configfile:
                config.write(configfile)
        
        return self.index()
