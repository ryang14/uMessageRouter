import _thread
from uMessageRouter import Router

router = Router()

def workerThread():
    while True:
        print(_thread.getmsg())
        _thread.wait()

threadID = _thread.start_new_thread("Thread", workerThread, ())
router.subscribe("test", threadID)

router.publish("test", "test")