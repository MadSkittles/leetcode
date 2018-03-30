class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        self.sum = []
        self.f(root)
        from collections import Counter
        c = Counter(self.sum)
        frequency = max(c.values())
        return [i for i in c if c[i] == frequency]

    def f(self, node):
        if not node:
            return 0
        res = self.f(node.left) + node.val + self.f(node.right)
        self.sum.append(res)
        return res