class Solution:
    def leastInterval(self, tasks, n):
        import heapq
        from collections import Counter
        q = [(-y, x) for x, y in Counter(tasks).items()]
        heapq.heapify(q)
        res = 0
        while q:
            k, next_q = n + 1, []
            while k and q:
                freq, c = heapq.heappop(q)
                freq += 1
                next_q.append((freq, c))
                k -= 1
                res += 1
            for f, c in next_q:
                if f:
                    heapq.heappush(q, (f, c))
            if q:
                res += k
        return res