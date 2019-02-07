import _thread

# Monitor selected topics
class Log:
    def __init__(self, router, topics):
        self.threadID = _thread.start_new_thread("Debug", self.run, (router,))
        for topic in topics:
            router.subscribe(topic, self.threadID)

    def run(self, router):
        while True:
            topic, message = router.checkMessages(wait = True)
            print("Message: " + message + " from topic: " + topic)
