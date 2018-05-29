class Solution:
    def findIntegers(self, num):
        s = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
        res, num, flag = 1, list(bin(num)[2:]), False
        for i, n in enumerate(num):
            if i == 0 or (num[i - 1] == '0' and (flag or num[i] == '1')):
                num[i] = '1'
                res += s[len(num) - i - 1]
            elif i > 0 and num[i - 1] == '1':
                flag = flag or num[i] == '1'
                num[i] = '0'
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findIntegers(999999999))
