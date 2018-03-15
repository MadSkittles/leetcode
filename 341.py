class NestedInteger(object):
    def __init__(self, val):
        self.val = val

    def isInteger(self):
        return isinstance(self.val, int)

    def getInteger(self):
        return self.val if self.isInteger() else None

    def getList(self):
        return self.val if not self.isInteger() else None

    @classmethod
    def val2nestedInteger(cls, v):
        if isinstance(v, int):
            return cls(v)
        else:
            res = []
            for i in v:
                res.append(cls.val2nestedInteger(i))
            return cls(res)

    @classmethod
    def list2nestedList(cls, l):
        res = []
        for v in l:
            res.append(cls.val2nestedInteger(v))
        return res


class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.iter = iter(nestedList)
        self.val = self.move_to_next()

    def move_to_next(self):
        while True:
            cur_val = next(self.iter, None)
            if cur_val is None:
                if len(self.stack):
                    self.iter = self.stack.pop()
                else:
                    return None
            elif cur_val.isInteger():
                return cur_val.getInteger()
            else:
                self.stack.append(self.iter)
                self.iter = iter(cur_val.getList())

    def next(self):
        res = self.val
        self.val = self.move_to_next()
        return res

    def hasNext(self):
        return self.val is not None


if __name__ == '__main__':
    i, v = NestedIterator(NestedInteger.list2nestedList([[], 1])), []
    while i.hasNext():
        v.append(i.next())
    print(v)
