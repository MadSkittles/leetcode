from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        c_a, c_b = Counter(A.split()), Counter(B.split())
        return [word for word, cnt in c_a.items() if cnt == 1 and word not in c_b] + [word for word, cnt in c_b.items() if cnt == 1 and word not in c_a]


if __name__ == "__main__":
    solution = Solution()
    print(solution.uncommonFromSentences(A="this apple is sweet", B="this apple is sour"))
    print(solution.uncommonFromSentences(A="apple apple", B="banana"))

