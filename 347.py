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

    class _Node:
        def __init__(self, val):
            self.val = val
            self.left = self.right = None
            self.left_size = self.right_size = 0

    def topKFrequent2(self, nums, k):
        if not nums:
            return []
        from collections import Counter
        c = Counter(nums)
        frequency = list(c.items())
        self.tree = None
        for val in frequency:
            self.build_bst(self.tree, val)
        return self.find_top_k(self.tree, k)

    def build_bst(self, node, val):
        if self.tree is None:
            self.tree = self._Node(val)
            return
        if val[1] < node.val[1]:
            node.left_size += 1
            if node.left:
                self.build_bst(node.left, val)
            else:
                node.left = self._Node(val)
        else:
            node.right_size += 1
            if node.right:
                self.build_bst(node.right, val)
            else:
                node.right = self._Node(val)

    def find_top_k(self, node, k):
        if not node:
            return []
        if node.right_size >= k:
            return self.find_top_k(node.right, k)
        if node.right_size + 1 == k:
            return [node.val[0]] + self.find_top_k(node.right, k - 1)
        return [node.val[0]] + self.find_top_k(node.right, node.right_size) + self.find_top_k(node.left, k - 1 - node.right_size)


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
