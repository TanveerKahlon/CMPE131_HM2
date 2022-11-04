from log import timestamp
import time

# defining a decorator
def timeme(func): 
    print(time.ctime())
    func()
