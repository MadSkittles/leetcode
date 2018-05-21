class Solution:
    def removeDuplicateLetters(self, s):
        from collections import Counter
        cnt = Counter(s)
        stack, shown = [], Counter()
        for c in s:
            if shown[c]:
                cnt[c] -= 1
                continue
            while stack and c < stack[-1] and cnt[stack[-1]] > 1:
                x = stack.pop()
                cnt[x] -= 1
                shown[x] -= 1
            stack.append(c)
            shown[c] += 1
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicateLetters('abacb'))
    print(solution.removeDuplicateLetters('baab'))
    print(solution.removeDuplicateLetters('bcabc'))
    print(solution.removeDuplicateLetters('cbacdcbc'))
