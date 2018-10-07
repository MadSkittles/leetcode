class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.max_size = k
        self.size = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value):
        if self.size == self.max_size:
            return False
        self.size += 1
        self.tail = (self.tail + 1) % self.max_size
        self.q[self.tail] = value
        return True

    def deQueue(self):
        if self.size == 0:
            return False
        self.size -= 1
        self.head = (self.head + 1) % self.max_size
        return True

    def Front(self):
        if self.size == 0:
            return -1
        return self.q[self.head]

    def Rear(self):
        if self.size == 0:
            return -1
        return self.q[self.tail]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size


if __name__ == "__main__":
    circularQueue = MyCircularQueue(8)
    print(circularQueue.enQueue(3))
    print(circularQueue.enQueue(9))
    print(circularQueue.enQueue(5))
    print(circularQueue.enQueue(0))
    print(circularQueue.deQueue())
    print(circularQueue.deQueue())
    print(circularQueue.isEmpty())
    print(circularQueue.isEmpty())
    print(circularQueue.Rear())
    print(circularQueue.Rear())
    print(circularQueue.deQueue())
