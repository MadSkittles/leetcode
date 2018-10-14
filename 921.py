class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        for c in S:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minAddToMakeValid("())"))
    print(solution.minAddToMakeValid("((("))
    print(solution.minAddToMakeValid("()"))
    print(solution.minAddToMakeValid("()))(("))

