class Solution:
    def numberToWords(self, num):
        if num >= 10 ** 9:
            res = self.numberToWords(num // (10 ** 9)) + ' Billion ' + self.numberToWords(num % (10 ** 9))
        elif num >= 10 ** 6:
            res = self.numberToWords(num // (10 ** 6)) + ' Million ' + self.numberToWords(num % (10 ** 6))
        elif num >= 10 ** 3:
            res = self.numberToWords(num // (10 ** 3)) + ' Thousand ' + self.numberToWords(num % (10 ** 3))
        elif num >= 10 ** 2:
            res = self.numberToWords(num // (10 ** 2)) + ' Hundred ' + self.numberToWords(num % (10 ** 2))
        elif num >= 20:
            m = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
            res = m[num // 10] + ' ' + self.numberToWords(num % 10)
        elif num > 0:
            m = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
            res = m[num]
        else:
            res = 'Zero'
        if num > 0 and res.endswith('Zero'):
            res = res.strip('Zero')
        return res.strip()


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberToWords(0))
    print(solution.numberToWords(15))
    print(solution.numberToWords(21))
    print(solution.numberToWords(100))
    print(solution.numberToWords(110))
    print(solution.numberToWords(120))
    print(solution.numberToWords(121))
    print(solution.numberToWords(1000))
    print(solution.numberToWords(1100))
    print(solution.numberToWords(1110))
    print(solution.numberToWords(1121))
    print(solution.numberToWords(11121))
    print(solution.numberToWords(111121))
    print(solution.numberToWords(1111121))
    print(solution.numberToWords(11111121))
    print(solution.numberToWords(111111121))
    print(solution.numberToWords(1111111121))
    print(solution.numberToWords(2 ** 31 - 1))
