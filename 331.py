class Solution:
    def isValidSerialization(self, preorder):
        self.preorder = preorder.split(',')[::-1]
        return self.f() and not self.preorder

    def f(self):
        if not self.preorder:
            return False
        res = self.preorder.pop()
        if res == '#':
            return True
        return self.f() and self.f()

    def isValidSerialization1(self, preorder):
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
