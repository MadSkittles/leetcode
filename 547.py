class Solution:
    def findCircleNum(self, M):
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