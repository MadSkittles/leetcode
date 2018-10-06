class MyCircularDeque:
    def __init__(self, k):
        self.max_size = k
        self.size = 0
        self.queue = [0] * k
        self.head = 0
        self.tail = k - 1

    def insertFront(self, value):
        if self.size == self.max_size:
            return False
        self.size += 1
        self.head = (self.head - 1 + self.max_size) % self.max_size
        self.queue[self.head] = value
        return True

    def insertLast(self, value):
        if self.size == self.max_size:
            return False
        self.size += 1
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        return True

    def deleteFront(self):
        if self.size == 0:
            return False
        self.size-=1
        self.head = (self.head + 1) % self.max_size
        return True

    def deleteLast(self):
        if self.size == 0:
            return False
        self.size-=1
        self.tail = (self.tail - 1 + self.max_size) % self.max_size
        return True

    def getFront(self):
        if self.size == 0:
            return -1
        return self.queue[self.head]

    def getRear(self):
        if self.size == 0:
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size


if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))
    print(circularDeque.insertLast(2))
    print(circularDeque.insertFront(3))
    print(circularDeque.insertFront(4))
    print(circularDeque.getRear())
    print(circularDeque.isFull())
    print(circularDeque.deleteLast())
    print(circularDeque.insertFront(4))
    print(circularDeque.getFront())
