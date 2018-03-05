class Solution:
    def evalRPN(self, tokens):
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}
        stack = []
        for t in tokens:
            if t in op:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(op[t](num1, num2)))
            else:
                stack.append(int(t))
        return stack[0]