class Solution:
    def isValidSerialization(self, preorder):
        preorder = preorder.split(',')
        if not preorder:
            return True
        if preorder[0] == '#':
            return len(preorder) == 1
        from queue import Queue
        q = Queue()
        q.put(preorder[0])
        index = 1
        while not q.empty():
            q.get()
            if index + 1 < len(preorder):
                for i in range(2):
                    if preorder[index + i] != '#':
                        q.put(preorder[index + i])
                index += 2
            else:
                return False
        return index >= len(preorder)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
    print(solution.isValidSerialization('1,#'))
    print(solution.isValidSerialization('9,#,#,1'))
