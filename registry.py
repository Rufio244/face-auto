class Registry:

    def __init__(self):
        self.store = {}

    def register(self, name, func):
        self.store[name] = func

    def get(self, name):
        return self.store.get(name)

    def exists(self, name):
        return name in self.store


registry = Registry()
