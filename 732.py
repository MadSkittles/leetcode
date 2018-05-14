class MyCalendarThree:

    def __init__(self):
        from collections import defaultdict
        self.cal = defaultdict(lambda: 0)
        self.res = 0

    def book(self, start, end):
        self.cal[start] += 1
        self.cal[end] -= 1
        cnt = 0
        for k in sorted(self.cal.keys()):
            cnt += self.cal[k]
            if start <= k < end and cnt > self.res:
                self.res = cnt
        return self.res


if __name__ == '__main__':
    cal = MyCalendarThree()
    print(cal.book(10, 20))
    print(cal.book(50, 60))
    print(cal.book(10, 40))
    print(cal.book(5, 15))
    print(cal.book(5, 10))
    print(cal.book(25, 55))
