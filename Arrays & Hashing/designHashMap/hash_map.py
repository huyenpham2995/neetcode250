class MyHashMap:

    def __init__(self):
        map_size = 1000001 # 10^6+1
        self.map = [-1]*map_size

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1