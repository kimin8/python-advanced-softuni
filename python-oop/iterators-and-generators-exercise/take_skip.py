class TakeSkip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.count:
            idx = self.idx
            self.idx += 1
            return idx * self.step
        else:
            self.idx = 0
            raise StopIteration
