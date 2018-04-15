class Solution:
    def reorganizeString(self, S):
        from collections import Counter
        from queue import PriorityQueue
        cnt, pq = Counter(S), PriorityQueue()
        for c, num in cnt.items():
            pq.put((-num, c))
        res = ''
        while not pq.empty():
            next, index = [], 0
            while index < 2 and not pq.empty():
                _, c = pq.get()
                if res and c == res[-1]:
                    return ''
                res += c
                cnt[c] -= 1
                index += 1
                if cnt[c] > 0:
                    next.append((-cnt[c], c))
            for item in next:
                pq.put(item)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorganizeString("vvvlo"))
