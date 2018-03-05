class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)

        base = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        mul_ten = 0

        while denominator % 10 == 0:
            denominator //= 10
            mul_ten += 1
        while numerator % 10 == 0:
            numerator //= 10
            mul_ten -= 1

        n = numerator
        result, rest, repeat = [], [n], None
        while True:
            cur_mul_ten = 0
            prefix_zero = ''
            while n < denominator:
                n *= 10
                mul_ten += 1
                cur_mul_ten += 1
                if cur_mul_ten > 1:
                    prefix_zero += '0'

            digit = prefix_zero + str(n // denominator)
            result.append(digit)

            if n % denominator == 0:
                break
            n = n % denominator

            tmp, tmp_mul_ten = n, 0
            while tmp % 10 == 0:
                tmp //= 10
                tmp_mul_ten += 1
            if tmp in rest:
                index = rest.index(tmp)
                repeat = result[index][tmp_mul_ten:] + ''.join(result[index + 1:])
                break

            rest.append(n)

        digits = ''.join(result)
        if mul_ten >= len(digits):
            result = '0.' + (mul_ten - len(digits)) * '0' + digits
        else:
            result = digits[:-mul_ten] + '.' + digits[-mul_ten:]
        if repeat is not None:
            d = result.index(repeat)
            result = result[:d] + '(' + result[d:] + ')'
        return ('-' if base else '') + result


if __name__ == '__main__':
    solution = Solution()
    print(solution.fractionToDecimal(1, 214748364))
    print(solution.fractionToDecimal(1, 90))
    print(solution.fractionToDecimal(1, 99))
    print(solution.fractionToDecimal(1, 17))
