class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        from queue import Queue
        q, visited = Queue(), set()
        q.put(('0000', 0))
        while not q.empty():
            slots, step = q.get()
            for i in range(4):
                for d in [-1, 1]:
                    s = slots[:i] + str((int(slots[i]) + 10 + d) % 10) + slots[i + 1:]
                    if s not in visited and s not in deadends:
                        if s == target:
                            return step + 1
                        q.put((s, step + 1))
                        visited.add(s)
        return -1