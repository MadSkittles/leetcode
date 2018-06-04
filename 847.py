class Solution:
    def shortestPathLength(self, graph):
        N = len(graph)
        new_g = [set() for _ in range(N)]
        for i in range(N):
            for j in graph[i]:
                new_g[i].add(j)
                new_g[j].add(i)
        graph = new_g

        M = (1 << N)
        dp = [[float('inf')] * N for _ in range(M)]

        from queue import Queue
        q = Queue()
        for i in range(N):
            dp[1 << i][i] = 0
            q.put((i, 1 << i))

        while not q.empty():
            node, state = q.get()
            steps = dp[state][node]
            for x in graph[node]:
                new_state = state | (1 << x)
                if dp[new_state][x] == float('inf'):
                    dp[new_state][x] = steps + 1
                    q.put((x, new_state))

        return min(dp[-1])
