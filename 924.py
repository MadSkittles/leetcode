from queue import Queue


class Solution:
    def minMalwareSpread(self, graph, initial):
        initial.sort()
        N, min_infected, res = len(graph), float("inf"), None
        for i in initial:
            visited = set()
            for node in initial:
                if node == i or node in visited:
                    continue
                q = Queue()
                q.put(node)
                visited.add(node)
                while not q.empty():
                    cur_node = q.get()
                    for k in range(N):
                        if graph[cur_node][k] == 1 and k not in visited:
                            q.put(k)
                            visited.add(k)
            if len(visited) < min_infected:
                min_infected, res = len(visited), i
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMalwareSpread([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1]], [5, 0]))
