import time
import threading

lock = threading.Lock()

def log(info):
    lock.acquire() # will block if lock is already held
    print time.strftime('%X %x'), info
    lock.release()

def setPath():
    import sys
    #TODO: RELATIVE PATH NEEDED !!
    sys.path.append('/home/kaisen/TestHard/framework/')
    
