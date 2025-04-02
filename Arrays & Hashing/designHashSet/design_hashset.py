class MyHashSet:
    def __init__(self):
        self.set_size = 1000001
        self.set = [False] * self.set_size

    def add(self, key: int) -> None:
        index = key % self.set_size
        self.set[index] = True

    def remove(self, key: int) -> None:
        self.set[key%self.set_size] = False

    def contains(self, key: int) -> bool:
        return self.set[key%self.set_size]