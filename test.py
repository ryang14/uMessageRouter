import _thread
from router import Router
from log import Log

router = Router()
logger = Log(router, '*')

def workerThread():
    while True:
        print(router.checkMessages(wait = True))

threadID = _thread.start_new_thread("Thread", workerThread, ())
router.subscribe("test", threadID)

router.publish("test", "test")