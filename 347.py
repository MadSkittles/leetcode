class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        return [i[0] for i in Counter(nums).most_common(k)]

    def topKFrequent1(self, nums, k):
        from collections import Counter
        c = Counter(nums)
        frequency = list(c.items())
        i, j = 0, len(frequency) - 1
        while True:
            while i < j:
                while i < j:
                    if frequency[i][1] > frequency[j][1]:
                        frequency[i], frequency[j] = frequency[j], frequency[i]
                        i += 1
                        break
                    else:
                        j -= 1
                while i < j:
                    if frequency[i][1] > frequency[j][1]:
                        frequency[i], frequency[j] = frequency[j], frequency[i]
                        j -= 1
                        break
                    else:
                        i += 1
            if i < len(frequency) - k:
                i, j = i + 1, len(frequency) - 1
            elif i > len(frequency) - k:
                i, j = 0, i - 1
            else:
                return [n[0] for n in frequency[i:]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
