class RandomizedSet:

    def __init__(self):
        self.dict = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            self.list[index] = self.list[-1]
            self.dict[self.list[-1]] = index
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.list[random.randrange(0, len(self.list))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()