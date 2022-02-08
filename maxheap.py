class MaxHeap():
    def __init__(self):
        self.items = [None]
    def add(self, data, value):
        self.items.append((data, value))
        