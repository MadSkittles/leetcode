class Solution:
    def nextGreaterElement(self, n):
        from functools import reduce
        l = []
        while n:
            l.append(n % 10)
            n //= 10
        l, i = l[::-1], len(l) - 2
        while i >= 0 and l[i + 1] <= l[i]:
            i -= 1
        if i < 0:
            return -1
        j = len(l) - 1
        while l[j] <= l[i]:
            j -= 1
        l[i], l[j] = l[j], l[i]
        l[i + 1:] = reversed(l[i + 1:])
        res = reduce(lambda x, y: x * 10 + y, l)
        return res if res <= (2 ** 31 - 1) else -1