class Keylistener:
    def __init__(self):
        self.keys:list[int] = []

    def add_key(self,key):
        if key not in self.keys:
            self.keys.append(key)

    def remove_key(self, key):
        if key in self.keys:
            self.keys.remove(key)

    def keypressed(self, key):
        return key in self.keys

    def clear(self):
        self.keys.clear()