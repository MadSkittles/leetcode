class Solution:
    def constructArray(self, n, k):
        diff, m = [], 1
        for i in range(k, 0, -1):
            diff.append(i * m)
            m = 0 - m
        res, index = [1], 0
        while len(res) < n:
            if index % k == 0 and index > 0:
                res.append(res[-k] + 1)
            if res[-1] + diff[index % k] > n:
                break
            res.append(res[-1] + diff[index % k])
            index += 1
        return res + list(range(max(res) + 1, n + 1))


if __name__ == '__main__':
    solution = Solution()
    print(solution.constructArray(10, 9))
