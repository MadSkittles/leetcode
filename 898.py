class Solution:
    def subarrayBitwiseORs(self, A):
        res, pre = set(), set()
        for n in A:
            pre = {n} | {n | m for m in pre}
            res.update(pre)
        return len(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarrayBitwiseORs([1, 1, 2]))
    print(solution.subarrayBitwiseORs([1, 2, 4]))

