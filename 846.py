class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand) % W:
            return False
        from collections import Counter
        from queue import PriorityQueue
        q, cnt = PriorityQueue(), Counter(hand)
        for n in cnt:
            q.put(n)
        while not q.empty():
            l = []
            while len(l) < W and not q.empty():
                n = q.get()
                if l and n != l[-1] + 1:
                    return False
                else:
                    l.append(n)
            if len(l) < W:
                return False
            for n in l:
                cnt[n] -= 1
                if cnt[n]:
                    q.put(n)
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))
