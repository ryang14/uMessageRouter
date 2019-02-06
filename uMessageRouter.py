import _thread

class Router:
    def __init__(self):
        self.subscriptions = dict()

    # Add a thread to a topic list creating the list if it does not exist
    def subscribe(self, topic, thread):
        if not topic in self.subscriptions:
            self.subscriptions[topic] = {thread}
        else:
            self.subscriptions[topic].append(thread)

    # Send a message to all threads subscribed to a topic and resume them in case they were waiting
    def publish(self, topic, message):
        if topic in self.subscriptions:
            for thread in self.subscriptions[topic]:
                _thread.notify(thread, _thread.RESUME) # Resume the task
                _thread.sendmsg(thread, message)
