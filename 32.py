class Solution:
    def longestValidParentheses(self, s):
        cnt, stack = 0, []
        for c in s:
            if c == ')':
                if len(stack) > 1 and type(stack[-1]) is int and stack[-2] == '(':
                    v = stack.pop()
                    stack.pop()
                    self.append(stack, v + 2)
                    continue
                elif stack and stack[-1] == '(':
                    stack.pop()
                    self.append(stack, 2)
                    continue
            stack.append(c)
        return max([v if type(v) is int else 0 for v in stack], default=0)

    def append(self, stack, cnt):
        if not cnt:
            return
        if not stack or type(stack[-1]) is not int:
            stack.append(cnt)
        else:
            stack[-1] += cnt


if __name__ == '__main__':
    solution = Solution()
    # print(solution.longestValidParentheses('(()'))
    # print(solution.longestValidParentheses(')()())'))
    print(solution.longestValidParentheses('(()())'))
