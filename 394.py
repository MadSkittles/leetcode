class Solution:
    def decodeString(self, s):
        stack = []
        for c in s:
            if c == ']':
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                times = ''
                while len(stack) and stack[-1].isdigit():
                    times = stack.pop() + times
                stack.append(int(times) * string)
            else:
                stack.append(c)
        from functools import reduce
        return reduce(lambda x, y: x + y, stack, '')


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
