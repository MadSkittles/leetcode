class Solution:
    def numSpecialEquivGroups(self, A):
        m = {self.gen_key(s) for s in A}
        return len(m)

    def gen_key(self, s):
        even_s = sorted(s[::2])
        odd_s = sorted(s[1::2])
        return "".join(odd_s), "".join(even_s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))
    print(solution.numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))
    print(solution.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))
    print(solution.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))
