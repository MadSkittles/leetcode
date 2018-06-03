class Solution:
    def backspaceCompare(self, S, T):
        stack1, stack2 = [], []
        for c in S:
            if c != '#':
                stack1.append(c)
            elif stack1:
                stack1.pop()
        for c in T:
            if c != '#':
                stack2.append(c)
            elif stack2:
                stack2.pop()
        return stack1 == stack2


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare("a##c", T = "#a#c"))
