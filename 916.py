import operator
from collections import Counter
from functools import reduce


class Solution:
    def wordSubsets(self, A, B):
        ctr_b = reduce(operator.or_, map(Counter, B))
        return [a for a in A if Counter(a) & ctr_b == ctr_b]


if __name__ == "__main__":
    solution = Solution()
    print(solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
    print(solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
    print(solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]))
    print(solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]))
    print(solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"]))
