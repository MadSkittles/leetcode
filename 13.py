class Solution(object):
    def romanToInt(self, s):
        keys = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        m = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        res, index = 0, 0
        while s:
            while index < len(keys) and not s.startswith(keys[index]):
                index += 1
            res += m[keys[index]]
            s = s[len(keys[index]):]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('III'))
    print(solution.romanToInt('IV'))
    print(solution.romanToInt('IX'))
    print(solution.romanToInt('LVIII'))
    print(solution.romanToInt('MCMXCIV'))
