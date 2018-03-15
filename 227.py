class Solution:
    def calculate(self, s):
        s = [c for c in s if c != ' ']
        op_map = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}
        from collections import deque
        num, stack = '', deque()
        for i, c in enumerate(s):
            if c in op_map:
                stack.append(c)
            else:
                num += c
                if i + 1 >= len(s) or s[i + 1] in op_map:
                    cur_num = int(num)
                    if len(stack) and stack[-1] in op_map and (stack[-1] == '*' or stack[-1] == '/'):
                        op, pre_num = stack.pop(), stack.pop()
                        stack.append(op_map[op](pre_num, cur_num))
                    else:
                        stack.append(cur_num)
                    num = ''
        while len(stack) > 1:
            pre_num, op, cur_num = stack.popleft(), stack.popleft(), stack.popleft()
            stack.appendleft(op_map[op](pre_num, cur_num))
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate('3+2*2'))
    print(solution.calculate('3/2'))
    print(solution.calculate('3+5 / 2'))
    print(solution.calculate('5/2*3'))
