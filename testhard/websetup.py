"""Setup the TestHard application"""
import logging

from testhard.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup testhard here"""
    load_environment(conf.global_conf, conf.local_conf)

    RepositoryController.repositoryList = ['svn', 'git']


