class Solution:
    def maxEnvelopes(self, envelopes: list):
        import bisect
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for i in range(0, len(envelopes)):
            height = envelopes[i][1]
            j = bisect.bisect_left(tails, height)
            if j == len(tails):
                tails.append(height)
            else:
                tails[j] = height
        return len(tails)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxEnvelopes([[5, 4], [6, 2], [6, 7], [2, 3]]))
