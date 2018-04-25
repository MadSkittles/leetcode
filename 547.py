class Solution:
    def findCircleNum(self, M):
        self.pre = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] and self.pre[i] != self.pre[j]:
                    self.union(self.pre[i], self.pre[j])
        return len(set(self.pre))

    def union(self, a, b):
        for i, v in enumerate(self.pre):
            if v == a:
                self.pre[i] = b

    def findCircleNum1(self, M):
        from queue import Queue
        q, visited, res = Queue(), set(), 0
        for i in range(len(M)):
            if i not in visited:
                res += 1
                visited.add(i)
                q.put(i)
                while not q.empty():
                    cur = q.get()
                    for j in range(len(M)):
                        if M[cur][j] and j not in visited:
                            visited.add(j)
                            q.put(j)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
