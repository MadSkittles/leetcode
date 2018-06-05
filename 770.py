class Solution:
    def basicCalculatorIV(self, expression: str, evalvars, evalints):
        expression = expression.replace('(', '( ').replace(')', ' )')
        m = dict(zip(evalvars, evalints))
        stack = []
        from collections import Counter
        for c in expression.split():
            if c:
                if c in {'(', '+', '-', '*'}:
                    stack.append(c)
                elif c == ')':
                    s = []
                    while stack and stack[-1] != '(':
                        s.append(stack.pop())
                    stack.pop()
                    stack.append(self.cal_exp(s[::-1]))
                elif c.isdigit():
                    stack.append((Counter(), int(c)))
                elif c in m:
                    stack.append((Counter(), m[c]))
                else:
                    stack.append((Counter({(c,): 1}), 0))
        elements, const = self.cal_exp(stack)
        return [str(elements[e]) + '*' + '*'.join(e) for e in sorted(elements.keys(), key=lambda x: (-len(x), x)) if elements[e]] + ([str(const)] if const else [])

    def cal_exp(self, exp):
        index = 1
        while index < len(exp):
            if exp[index] == '*':
                exp[index - 1:index + 2] = [self.mul(exp[index - 1], exp[index + 1])]
                index -= 2
            index += 2
        from collections import Counter
        elements, sum = Counter(), 0
        index = 0
        while index < len(exp):
            base = -1 if index > 0 and exp[index - 1] == '-' else 1
            c, const = exp[index]
            sum += base * const
            for e in c:
                elements[e] += base * c[e]
            index += 2
        return (elements, sum)

    def mul(self, val1, val2):
        elements1, const1 = val1
        elements2, const2 = val2
        from collections import Counter
        elements = Counter()
        for e1 in elements1:
            for e2 in elements2:
                elements[tuple(sorted(e1 + e2))] += elements1[e1] * elements2[e2]
        if const2:
            for e1 in elements1:
                elements[e1] += const2 * elements1[e1]
        if const1:
            for e2 in elements2:
                elements[e2] += const1 * elements2[e2]
        return (elements, const1 * const2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.basicCalculatorIV(expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                                     evalvars=[], evalints=[]))
