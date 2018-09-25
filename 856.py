class Solution:
    def scoreOfParentheses(self, S):
        stack = [0]

        def helper(element):
            if element == ")":
                if stack[-1] == "(":
                    stack.pop()
                    helper(1)
                else:
                    n = stack.pop()
                    stack.pop()
                    helper(2 * n)
            else:
                if stack and stack[-1] != "(":
                    n = stack.pop()
                    helper(n + element)
                else:
                    stack.append(element)

        for c in S:
            if c == ")":
                helper(")")
            else:
                stack.append(c)
        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.scoreOfParentheses(""))
