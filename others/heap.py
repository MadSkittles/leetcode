class Heap:
    def __init__(self, l: list):
        self.l = l
        self.heapify()

    def top_adjust(self, cur=0, length=None):
        length = len(self.l) if length is None else length
        child = 2 * cur + 1
        while child < length:
            if child < length - 1 and self.l[child] > self.l[child + 1]:
                child += 1
            if self.l[cur] > self.l[child]:
                self.l[cur], self.l[child] = self.l[child], self.l[cur]
                cur, child = child, 2 * child + 1
            else:
                break

    def bottom_adjust(self):
        cur = len(self.l) - 1
        parent = (cur - 1) // 2
        while cur > 0 and self.l[cur] < self.l[parent]:
            self.l[cur], self.l[parent] = self.l[parent], self.l[cur]
            cur, parent = parent, (parent - 1) // 2

    def heapify(self):
        for i in range((len(self.l) - 1) // 2, -1, -1):
            self.top_adjust(i)

    def pop(self):
        if len(self.l) == 0:
            raise IndexError
        if len(self.l) == 1:
            return self.l.pop()
        val = self.l[0]
        self.l[0] = self.l.pop()
        self.top_adjust()
        return val

    def push(self, val):
        self.l.append(val)
        if len(self.l) > 1:
            self.l[0], self.l[-1] = self.l[-1], self.l[0]
        self.bottom_adjust()

    def __str__(self):
        return str(self.l)

    __repr__ = __str__


if __name__ == '__main__':
    heap = Heap([32, 66, 45, 12, 32, 34, 78, 51, 31, 34])
    print(heap)
    heap.push(9)
    print(heap)
    heap.push(33)
    print(heap)
