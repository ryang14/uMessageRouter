import _thread
import json

class Router:
    def __init__(self):
        self.subscriptions = dict()

    # Add a thread to a topic list creating the list if it does not exist
    # Can be called anywhere
    def subscribe(self, topic, thread):
        if not topic in self.subscriptions:
            self.subscriptions[topic] = [thread]
        else:
            self.subscriptions[topic].append(thread)

    # Send a message to all threads subscribed to a topic and resume them in case they were waiting
    # Called from publishing task
    def publish(self, topic, message):
        if topic in self.subscriptions:
            for thread in self.subscriptions[topic]:
                _thread.notify(thread, _thread.RESUME) # Resume the task
                _thread.sendmsg(thread, json.dumps({"topic": topic, "message": message})) # Encode topic and message
        
        # Publish every message to the wildcard topic
        if "*" in self.subscriptions:
            for thread in self.subscriptions["*"]:
                _thread.notify(thread, _thread.RESUME) # Resume the task
                _thread.sendmsg(thread, json.dumps({"topic": topic, "message": message})) # Encode topic and message

    # Check for messages and extract the topic
    # Called from task
    # Retrurns (topic, message)
    def checkMessages(self, wait = False, timeout = None):
        if wait:
            # Wait for message
            if timeout:
                _thread.wait(timeout) 
            else:
                _thread.wait() 
        
        message_type, sender_ID, message_JSON = _thread.getmsg()

        if message_type == 2: # If the message is a string
            # Parse the topic and message
            msg = json.loads(message_JSON)
            topic = msg["topic"]
            message = msg["message"]
            return (topic, message)
        
        return (None, None)
