class Solution(object):
    def isValid(self, s):
        m, stack = {')': '(', '}': '{', ']': '['}, []
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                if not stack or stack[-1] != m[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()'))
    print(solution.isValid('()[]{}'))
    print(solution.isValid('(]'))
    print(solution.isValid('([)]'))
    print(solution.isValid('{[]}'))
