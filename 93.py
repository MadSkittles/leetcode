class Solution:
    def restoreIpAddresses(self, s):
        self.cache = {}
        return ['.'.join(ip) for ip in self.f(s, 4)]

    def f(self, s, left):
        if (s, left) in self.cache:
            return self.cache[(s, left)]

        res = []
        if left > 1:
            for i in range(1, 4):
                ip_part = s[:i]
                if left - 1 <= len(s) - i <= 3 * left - 3 and self.is_valid(ip_part):
                    res.extend([(ip_part, *j) for j in self.f(s[i:], left - 1)])
        elif left == 1 and self.is_valid(s):
            res = [(s,)]

        if (s, left) not in self.cache:
            self.cache[(s, left)] = res
        return res

    def is_valid(self, ip_part):
        return not (ip_part.startswith('0') and ip_part != '0') and 0 <= int(ip_part) <= 255


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("010010"))
