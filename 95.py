from common import TreeNode


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.f(list(range(1, n + 1)))

    def f(self, nodes):
        if len(nodes) == 0:
            return [None]
        if len(nodes) == 1:
            return [TreeNode(nodes[0])]
        else:
            res = []
            for index, n in enumerate(nodes):
                left_nodes = self.f(nodes[:index])
                right_nodes = self.f(nodes[index + 1:])
                for i in left_nodes:
                    for j in right_nodes:
                        node = TreeNode(n)
                        node.left = i
                        node.right = j
                        res.append(node)
            return res


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 4):
        print(solution.generateTrees(i))
