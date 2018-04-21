class Solution:
    def allPathsSourceTarget(self, graph):
        from queue import Queue
        q, res = Queue(), []
        q.put((0, (0,)))
        while not q.empty():
            from_, path = q.get()
            if from_ == len(graph) - 1:
                res.append(path)
                continue
            for to in graph[from_]:
                q.put((to, path + (to,)))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.allPathsSourceTarget([[1, 2], [3], [3], []]))
