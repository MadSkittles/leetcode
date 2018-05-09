class Solution:
    def maskPII(self, S):
        return self.mask_email(S) if '@' in S else self.mask_phone(S)

    def mask_email(self, S):
        import re
        parts = re.split('[@.]', S.lower())
        return '{}@{}.{}'.format(parts[0][0] + '*' * 5 + parts[0][-1], parts[1], parts[2])

    def mask_phone(self, S):
        digits = [c for c in S if c.isdigit()]
        pre = ''
        if len(digits) > 10:
            pre = '+' + '*' * (len(digits) - 10) + '-'
        return pre + '***-***-' + ''.join(digits[-4:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maskPII('LeetCode@LeetCode.com'))
    print(solution.maskPII('AB@qq.com'))
    print(solution.maskPII('1(234)567-890'))
    print(solution.maskPII('86-(10)12345678'))
