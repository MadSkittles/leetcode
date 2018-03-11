class Solution:
    def isAdditiveNumber(self, num):
        for i in range(1, len(num) // 2 + 1):
            for j in range(i + 1, len(num)):
                pre_pre, pre = num[:i], num[i:j]
                if (pre.startswith('0') and pre != '0') or (pre_pre.startswith('0') and pre_pre != '0'):
                    continue
                cur_num, total = num[j:], str(int(pre_pre) + int(pre))
                while cur_num.startswith(total):
                    cur_num = cur_num[len(total):]
                    if not len(cur_num):
                        return True
                    pre_pre, pre = pre, total
                    total = str(int(pre_pre) + int(pre))
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAdditiveNumber('123'))
