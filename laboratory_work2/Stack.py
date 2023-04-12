class Stack:
    def __init__(self, *elements):
        self._data = list(elements)

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def reverse(self):
        self._data.reverse()

    def add_last(self, *objects):
        for obj in objects:
            self._data.append(obj)

    def get_last(self):
        if not self.is_empty():
            return self._data[-1]

    def pop_last(self):
        if not self.is_empty():
            return self._data.pop()
