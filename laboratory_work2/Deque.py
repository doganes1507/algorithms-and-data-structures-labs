from Stack import Stack


class Deque(Stack):
    def add_first(self, *objects):
        for obj in objects:
            self._data.insert(0, obj)

    def get_first(self):
        if not self.is_empty():
            return self._data[0]

    def pop_first(self):
        if not self.is_empty():
            return self._data.pop(0)
