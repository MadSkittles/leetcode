class Solution:
    def solveEquation(self, equation):
        left_exp, right_exp = equation.split('=')
        d = {left_exp: [0, 0], right_exp: [0, 0]}
        for expression in (left_exp, right_exp):
            exp = ''
            for i, c in enumerate(expression + '+'):
                if c in '+-' and i > 0:
                    if exp[-1] == 'x':
                        exp = exp[:-1]
                        if not exp or not exp[-1].isdigit():
                            exp += '1'
                        d[expression][1] += int(exp)
                        exp = ''
                    else:
                        d[expression][0] += int(exp)
                        exp = ''
                exp += c
        x_n, n = d[left_exp][1] - d[right_exp][1], d[right_exp][0] - d[left_exp][0]
        if x_n == 0:
            return 'No solution' if n != 0 else 'Infinite solutions'
        else:
            return 'x=%d' % (n // x_n)
