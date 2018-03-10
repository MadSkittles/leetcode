class Iterator(object):
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        val = self.nums[self.index]
        self.index += 1
        return val


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.peek_val = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.peek_val

    def next(self):
        result = self.peek_val
        self.peek_val = self.iter.next() if self.iter.hasNext() else None
        return result

    def hasNext(self):
        return self.peek_val is not None

if __name__ == '__main__':
    solution=PeekingIterator(Iterator([1,2,3,4,5,6,7,8,9]))
    while solution.hasNext():
        print('peek:',solution.peek())
        print('value:', solution.next())