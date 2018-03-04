from common import TreeLinkNode


class Solution:
    def connect(self, root):
        if not root:
            return None
        p = [root]
        while p:
            res = []
            for index, node in enumerate(p):
                node.next = p[index + 1] if index + 1 < len(p) else None
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            p = res


if __name__ == '__main__':
    solution = Solution()
    tree = TreeLinkNode.list2Tree([1, 2, 3, 4, 5, 6, 7])
    solution.connect(tree)
    print(tree)
