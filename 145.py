from common import TreeNode


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
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
    print(TreeNode.list2Tree([1, None, 2, 3]))
    print(solution.postorderTraversal(TreeNode.list2Tree([1, None, 2, 3])))
