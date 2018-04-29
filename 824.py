class Solution:
    def toGoatLatin(self, S):
        S, res = S.split(), []
        for index, word in enumerate(S, 1):
            r = word
            if word[0].lower() not in {'a', 'e', 'i', 'o', 'u'}:
                r = word[1:] + word[0]
            res.append(r + 'ma' + 'a' * index)
        return ' '.join(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.toGoatLatin("I speak Goat Latin"))
    print(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"))
