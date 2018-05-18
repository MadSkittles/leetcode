class Solution:
    def largeGroupPositions(self, S):
        res, lo, S = [], 0, S + '#'
        for hi in range(len(S)):
            if S[hi] != S[lo]:
                if hi - lo >= 3:
                    res.append([lo, hi - 1])
                lo = hi
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.largeGroupPositions("abbxxxxzzy"))
    print(solution.largeGroupPositions("abc"))
    print(solution.largeGroupPositions("abcdddeeeeaabbbcd"))
