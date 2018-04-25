class Solution:
    def nextGreaterElement(self, n):
        from functools import reduce
        n = list(str(n))
        for i in range(len(n) - 2, -1, -1):
            if n[i] < n[i + 1]:
                j = len(n) - 1
                while n[j] <= n[i]:
                    j -= 1
                n[i], n[j] = n[j], n[i]
                n[i + 1:] = n[i + 1:][::-1]
                break
        else:
            return -1
        res = reduce(lambda x, y: int(x) * 10 + int(y), n)
        return res if res < (2 ** 31 - 1) else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElement(12))
