class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(self.iterable) - 1
        self.end = 0

    def restart_attributes(self):
        self.start = len(self.iterable) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            start = self.start
            self.start -= 1
            return self.iterable[start]
        else:
            self.restart_attributes()
            raise StopIteration
