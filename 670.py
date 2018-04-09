class Solution:
    def maximumSwap(self, num):
        max_num, num_list = [], []
        while num:
            n = num % 10
            max_num.append(max(n, max_num[-1] if max_num else float('-inf')))
            num_list.append(n)
            num //= 10
        max_num, num_list, pos = max_num[::-1], num_list[::-1], 0
        while pos < len(num_list) and num_list[pos] == max_num[pos]:
            pos += 1
        m, max_num, pos = {}, float('-inf'), pos - (pos >= len(num_list))
        for i in range(pos, len(num_list)):
            m.setdefault(num_list[i], []).append(i)
            max_num = max(max_num, num_list[i])
        swap_pos = m[max_num][-1]
        num_list[pos], num_list[swap_pos] = num_list[swap_pos], num_list[pos]
        from functools import reduce
        return reduce(lambda x, y: x * 10 + y, num_list, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSwap(98638))
