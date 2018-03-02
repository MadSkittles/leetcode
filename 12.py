# Integer to Roman

# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def intToRoman(self, num):
        rules = [('I', 'V'), ('X', 'L'), ('C', 'D'), 'M']
        result = ''
        index = 0
        while num > 0:
            result = self.getExpression(num % 10, rules[index],
                                        rules[index + 1] if index + 1 < len(rules) else None) + result
            num = int(num / 10)
            index += 1
        return result

    def getExpression(self, digit, rule, next_rule):
        if digit <= 3:
            return rule[0] * digit
        elif digit == 4:
            return rule[0] + rule[1]
        elif 5 <= digit <= 8:
            return rule[1] + rule[0] * (digit - 5)
        elif digit == 9:
            return rule[0] + next_rule[0]


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 4000):
        print('%d : %s' % (i, solution.intToRoman(i)))
