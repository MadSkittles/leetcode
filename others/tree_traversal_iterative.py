from common import TreeNode


class Solution(object):
    def LDR(self, root):
        res = []
        stack = [None]
        node = root
        while node:
            if node.left:
                stack.append(node)
                node = node.left
            else:
                while node and not node.right:
                    res.append(node.val)
                    node = stack.pop()
                if node:
                    res.append(node.val)
                node = node.right if node else node
        return res

    def DLR(self, root):
        res = []
        stack = [None]
        node = root
        while node:
            res.append(node.val)
            if node.left:
                stack.append(node)
                node = node.left
            else:
                while node and not node.right:
                    node = stack.pop()
                node = node.right if node else node
        return res

    def LRD(self, root):
        res, visited = [], set()
        stack = [root]
        node = root
        while len(stack):
            if node.left and node.left not in visited:
                stack.append(node)
                node = node.left
            elif node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                res.append(node.val)
                visited.add(node)
                node = stack.pop()
        return res


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.list2Tree([5, 3, 9, 2, 4, 7, 10, 1, None, None, None, 6, 8, None, 11])
    print(solution.LDR(tree))
    print(solution.DLR(tree))
    print(solution.LRD(tree))
