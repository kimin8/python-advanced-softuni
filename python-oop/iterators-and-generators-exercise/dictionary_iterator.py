class DictionaryIter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.dictionary.keys()):
            idx = self.idx
            self.idx += 1
            return list(self.dictionary.keys())[idx], self.dictionary[list(self.dictionary.keys())[idx]]
        else:
            self.idx = 0
            raise StopIteration

