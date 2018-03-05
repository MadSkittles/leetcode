class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        self.cache = {}
        return self.f(s)

    def f(self, left_s):
        if left_s in self.cache:
            return self.cache[left_s]

        if len(left_s) <= 0:
            return 1
        if left_s[0] == '0':
            return 0

        result = 0
        if left_s[0] == '1' and len(left_s) >= 2:
            result += self.f(left_s[2:])
        elif left_s[0] == '2' and len(left_s) >= 2 and left_s[1] <= '6':
            result += self.f(left_s[2:])
        result += self.f(left_s[1:])

        if left_s not in self.cache:
            self.cache[left_s] = result

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('0'))
