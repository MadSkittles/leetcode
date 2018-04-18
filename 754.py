class Solution:
    def reachNumber(self, target):
        import math
        t = abs(target)
        n = math.floor(math.sqrt(2 * t))
        while True:
            to_minus = ((n + 1) * n) / 2 - t
            if to_minus >= 0 and to_minus % 2 == 0:
                return int(n)
            n += 1
