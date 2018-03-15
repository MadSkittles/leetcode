class RandomizedSet:
    def __init__(self):
        self.data = set()

    def insert(self, val):
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True

    def remove(self, val):
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        from random import choice
        return choice(list(self.data))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()