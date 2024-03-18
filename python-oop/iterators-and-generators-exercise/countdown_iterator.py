class CountdownIterator:
    def __init__(self, count: int):
        self.count = count
        self.i = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return i
        else:
            self.i = self.count
            raise StopIteration
