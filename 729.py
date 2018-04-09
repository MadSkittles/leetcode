class MyCalendar:
    def __init__(self):
        self.start = []
        self.end = []

    def book(self, start, end):
        from bisect import bisect
        if not self.start:
            self.start.append(start)
            self.end.append(end)
            return True
        else:
            pos = bisect(self.start, start)
            if (pos >= 1 and start < self.end[pos - 1]) or (pos < len(self.start) and end > self.start[pos]):
                return False
            else:
                self.start.insert(pos, start)
                self.end.insert(pos, end)
                return True


if __name__ == '__main__':
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(15, 25))
    print(myCalendar.book(20, 30))
