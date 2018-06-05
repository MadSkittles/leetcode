class Solution:
    def calculate(self, s):
        if not s:
            return 0
        stack, num, s = [], '', s + ' '
        for c in s:
            if c.isdigit():
                num += c
            elif num:
                stack.append(int(num))
                num = ''
            if c == '+' or c == '-' or c == '(':
                stack.append(c)
            elif c == ')':
                s = []
                while stack and stack[-1] != '(':
                    s.append(stack.pop())
                stack.pop()
                stack.append(self.cal(s))
        return self.cal(stack[::-1])

    def cal(self, exp):
        while len(exp) >= 3:
            v1, op, v2 = exp.pop(), exp.pop(), exp.pop()
            exp.append(v1 + v2 if op == '+' else v1 - v2)
        return exp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate(""))
