class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, user):
        self.subscribers.add(user)

    def unregister(self, user):
        self.subscribers.discard(user)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)
