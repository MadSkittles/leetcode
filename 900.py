class RLEIterator:
    def __init__(self, A):
        self.data = []
        for i in range(0, len(A), 2):
            self.data.append([A[i], A[i + 1]])
        self.data.reverse()

    def next(self, n):
        res = -1
        while n and self.data:
            if n <= self.data[-1][0]:
                self.data[-1][0] -= n
                res, n = self.data[-1][1], 0
            else:
                n -= self.data[-1][0]
                self.data[-1][0] = 0
            if self.data[-1][0] == 0:
                self.data.pop()
        return res


if __name__ == "__main__":
    rleIterator = RLEIterator([3, 8, 0, 9, 2, 5])
    print(rleIterator.next(2))
    print(rleIterator.next(1))
    print(rleIterator.next(1))
    print(rleIterator.next(2))
