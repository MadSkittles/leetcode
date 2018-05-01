class MyCalendarTwo:

    def __init__(self):
        self.start = []
        self.end = []
        self.intersection_start = []
        self.intersection_end = []

    def book(self, start, end):
        from bisect import bisect
        if not self.start:
            self.start.append(start)
            self.end.append(end)
            return True
        elif not self.intersection_start:
            pos = insert_pos = bisect(self.start, start)
            while pos >= 1:
                if start < self.end[pos - 1]:
                    self.intersection_start.insert(0, start)
                    self.intersection_end.insert(0, min(self.end[pos - 1], end))
                pos -= 1
            pos = insert_pos
            while pos < len(self.start):
                if end > self.start[pos]:
                    self.intersection_start.append(self.start[pos])
                    self.intersection_end.append(min(self.end[pos], end))
                pos += 1
            self.start.insert(insert_pos, start)
            self.end.insert(insert_pos, end)
            return True
        else:
            intersection_pos = bisect(self.intersection_start, start)
            if (intersection_pos >= 1 and start < self.intersection_end[intersection_pos - 1]) or (intersection_pos < len(self.intersection_start) and end > self.intersection_start[intersection_pos]):
                return False
            else:
                pos = insert_pos = bisect(self.start, start)
                while pos >= 1:
                    if start < self.end[pos - 1]:
                        self.intersection_start.insert(intersection_pos, start)
                        self.intersection_end.insert(intersection_pos, min(self.end[pos - 1], end))
                    pos -= 1
                intersection_pos = bisect(self.intersection_start, start)
                pos = insert_pos
                while pos < len(self.start):
                    if end > self.start[pos]:
                        self.intersection_start.insert(intersection_pos, self.start[pos])
                        self.intersection_end.insert(intersection_pos, min(self.end[pos], end))
                    pos += 1
                    intersection_pos += 1
                self.start.insert(insert_pos, start)
                self.end.insert(insert_pos, end)
                return True


class MyCalendarTwo1:

    def __init__(self):
        from collections import Counter
        self.counter = Counter()

    def book(self, start, end):
        self.counter[start] += 1
        self.counter[end] -= 1
        cnt = 0
        for k in sorted(self.counter.keys()):
            cnt += self.counter[k]
            if cnt > 2:
                self.counter[start] -= 1
                if not self.counter[start]:
                    self.counter.pop(start)
                self.counter[end] += 1
                if not self.counter[end]:
                    self.counter.pop(end)
                return False
        return True
