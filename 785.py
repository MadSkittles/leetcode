class Solution:
    def isBipartite(self, graph):
        color = [0] * len(graph)
        from queue import Queue
        q = Queue()
        for start in range(len(graph)):
            if color[start] != 0:
                continue
            q.put(start)
            color[start] = 1
            while not q.empty():
                cur_node = q.get()
                for node in graph[cur_node]:
                    if color[node] == 0:
                        color[node] = 0 - color[cur_node]
                        q.put(node)
                    elif color[node] + color[cur_node] != 0:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
