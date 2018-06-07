class Solution:
    def cur_ver_edge(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.low = [0] * len(graph)
        self.dfn = [0] * len(graph)
        self.parent = [0] * len(graph)
        self.is_cut_ver = [False] * len(graph)
        self.cut_edge = []
        self.dfs()
        return [*filter(lambda x: self.is_cut_ver[x], range(len(graph)))], self.cut_edge

    def dfs(self):
        child_tree, self.visited[0], self.visite_order, self.parent[0] = 0, True, 1, -1
        for next in self.graph[0]:
            if not self.visited[next]:
                self.visited[next] = True
                self.parent[next] = 0
                self.dfs0(next)
                if self.low[next] > self.dfn[0]:
                    self.cut_edge.append((0, next))
                child_tree += 1
        if child_tree >= 2:
            self.is_cut_ver[0] = True

    def dfs0(self, node):
        self.visite_order += 1
        self.dfn[node] = self.low[node] = self.visite_order
        for next in self.graph[node]:
            if not self.visited[next]:
                self.visited[next] = True
                self.parent[next] = node
                self.dfs0(next)
                self.low[node] = min(self.low[node], self.low[next])

                if self.low[next] >= self.dfn[node]:
                    self.is_cut_ver[node] = True
                    if self.low[next] > self.dfn[node]:
                        self.cut_edge.append((node, next))
            elif self.parent[node] != next and self.dfn[next] < self.dfn[node]:
                self.low[node] = min(self.low[node], self.dfn[next])


if __name__ == '__main__':
    solution = Solution()
    print(solution.cur_ver_edge([[1, 2, 5, 6], [0], [0], [4, 5], [3, 5, 6], [0, 3, 4], [0, 4, 7, 9], [6, 8], [7], [6, 10, 11, 12], [9], [9, 12], [9, 11]]))
