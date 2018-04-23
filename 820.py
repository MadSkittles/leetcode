class Solution:
    def minimumLengthEncoding(self, words):
        words = sorted(word[::-1] for word in words)
        return sum(len(words[i]) + 1 if i + 1 >= len(words) or not words[i] == words[i + 1][:len(words[i])] else 0 for i in range(len(words)))

    def minimumLengthEncoding1(self, words):
        res, words, s = 0, sorted(words, key=len, reverse=True), set()
        for i in range(len(words)):
            if words[i] not in s:
                res += len(words[i]) + 1
                for j in range(len(words[i])):
                    s.add(words[i][j:])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumLengthEncoding1(["time", "me", "bell"]))
