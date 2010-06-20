import os

path = '/'+'/'.join(os.path.abspath(__file__).split('/')[1:-1])
logpath = path + '/log.txt'

def getLog():
    if os.path.exists(logpath):
        with open(logpath,'r') as f:
            return f.read()
    else:
        return None

def removeLog():
    if os.path.exists(logpath):
        os.remove(logpath)
