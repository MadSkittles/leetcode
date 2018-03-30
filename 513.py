class Solution:
    def findBottomLeftValue(self, root):
        result, result_floor = -1, -1
        from queue import Queue
        q = Queue()
        q.put((root, 0))
        while not q.empty():
            node, floor = q.get()
            if floor > result_floor:
                result = node.val
                result_floor = floor
            if node.left:
                q.put((node.left, floor + 1))
            if node.right:
                q.put((node.right, floor + 1))
        return result