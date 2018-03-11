class Solution:
    def maxProduct(self, words):
        w = {}
        for word in words:
            w[word] = set(word)
        max_product = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not w[words[i]].intersection(w[words[j]]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
