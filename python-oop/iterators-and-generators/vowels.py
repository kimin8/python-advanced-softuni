class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels_list = ['a', 'o', 'u', 'i', 'y', 'e']
        self.vowels = [x for x in list(string) if x.lower() in self.vowels_list]
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.vowels) - 1:
            self.idx += 1
            return self.vowels[self.idx]
        else:
            self.idx = -1
            raise StopIteration
