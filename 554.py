class Solution:
    def leastBricks(self, wall):
        from collections import Counter
        from itertools import accumulate
        c = Counter()
        for bricks in wall:
            c.update(accumulate(bricks, lambda x, y: x + y))
        c.pop(sum(wall[0]))
        return len(wall) - max(c.values(), default=0)