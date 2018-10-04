from queue import Queue

from common import TreeNode


class Solution:
    def distanceK(self, root, target, K):
        parent, flag, q, node = {}, True, Queue(), None
        q.put(root)
        while not q.empty() and not node:
            p = q.get()
            if p.val == target.val:
                node = p
                break
            for c in filter(lambda x: x is not None, [p.left, p.right]):
                parent[c.val] = p
                q.put(c)

        res, q, visited = [], Queue(), {node.val}
        q.put((node, 0))
        while not q.empty():
            p, dis = q.get()
            if dis == K:
                res.append(p.val)
                continue
            for next in filter(lambda x: x is not None and x.val not in visited, [p.left, p.right, parent.get(p.val, None)]):
                q.put((next, dis + 1))
                visited.add(next.val)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.distanceK(TreeNode.list2Tree([0, 1, None, None, 2, None, 3, None, 4]), TreeNode(3), 0))

