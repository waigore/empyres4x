class GenericIterator(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.count = 0

    def __next__(self):
        if self.count >= len(self.iterable):
            raise StopIteration

        v = self.iterable[self.count]
        self.count += 1
        return v
