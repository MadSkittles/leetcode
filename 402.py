class Solution:
    def removeKdigits(self, num, k):
        stack, i = [], 0
        while i <= len(num) and k:
            if len(stack) and (i == len(num) or num[i] < stack[-1]):
                stack.pop()
                k -= 1
            else:
                stack.append(num[i])
                i += 1
        return (''.join(stack) + num[i:]).lstrip('0') or '0'


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeKdigits("1234567890", 9))
    print(solution.removeKdigits("1432219", 3))
    print(solution.removeKdigits("10200", 1))
    print(solution.removeKdigits("112", 1))
