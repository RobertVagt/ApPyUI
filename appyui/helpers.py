class Settings:
    pass


class Dispatcher:
    def __init__(self):
        self._listeners = []

    def push(self, action, details):
        for listener in self._listeners:
            listener.handle_event(Event(action, details))

    def add_listener(self, listener):
        self._listeners.append(listener)


class Event:
    def __init__(self, action, details=None, source=None, is_synchronous=True):
        self.action = action
        self.details = details
        self.source = source
        self.is_synchronous = is_synchronous


