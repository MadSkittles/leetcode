from math import gcd


class Solution:
    def mirrorReflection(self, p, q):
        s = p * q // gcd(p, q)
        if not s % (2 * p):
            return 0
        return 1 if s % (2 * q) else 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.mirrorReflection(2, 1))

