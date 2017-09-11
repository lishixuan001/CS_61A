class OddNaturalsIterator():
    def __init__(self):
        self.current = 1
    def __next__(self):
        result = self.current
        self.current += 2
        return result
    def __iter__(self):
        return self

class EvenNaturalsIterator():
    def __init__(self):
        self.current = 0
    def __next__(self):
        result = self.current
        self.current += 2
        return result
    def __iter__(self):
        return EvenNaturalsIterator()
