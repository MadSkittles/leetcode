class Solution:
    def findMinHeightTrees(self, n, edges):
        graph,nodes = {},set(range(n))
        for start, end in edges:
            graph.setdefault(start, []).append(end)
            graph.setdefault(end, []).append(start)
        while len(nodes) > 2:
            leaves = []
            for start in graph:
                if start not in nodes:
                    continue
                if len(graph[start]) == 1:
                    leaves.append(start)
            for leaf in leaves:
                graph[graph[leaf][0]].remove(leaf)
                nodes.remove(leaf)
        return sorted(nodes)

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
