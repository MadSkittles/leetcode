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
