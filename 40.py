class Solution:
    def multiply(self, num1, num2):
        num1 = self.seprate(num1)
        num2 = self.seprate(num2)

        result_list = [0] * (len(num1) + len(num2) + 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = num1[i] * num2[j]
                result_list[i + j] += digit % 10000
                result_list[i + j + 1] += digit // 10000
        result = ''
        for i in range(len(result_list)):
            n = result_list[i]
            result = str(n % 10000).rjust(4, '0') + result
            if i + 1 < len(result_list):
                result_list[i + 1] += n // 10000
        return result.lstrip('0') or '0'


    def seprate(self, num):
        res = []
        for i in range(0, len(num), 4):
            start = len(num) - i - 4 if (len(num) - i - 4) >= 0 else 0
            end = len(num) - i
            res.append(int(num[start:end]))
        return res


if __name__ == '__main__':
    solution = Solution()
    a = '4723874982742975897897345897358371267682687621874230543535345346789789'
    b = '6496845864864989028427409274328478247829789237891732189361786375627527'
    print(int(a) * int(b))
    print(solution.multiply(a, b))
