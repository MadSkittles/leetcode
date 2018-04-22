class Solution:
    def eventualSafeNodes(self, graph):
        self.res = set()
        self.g, self.pre_g = {}, {}
        for from_, to_list in enumerate(graph):
            if to_list:
                self.g[from_] = set(to_list)
                for to in to_list:
                    self.pre_g.setdefault(to, set()).add(from_)
        for node in range(len(graph)):
            if node not in self.res and (node not in self.g or not self.g[node]):
                self.remove_node(node)
        return sorted(self.res)

    def remove_node(self, node):
        self.res.add(node)
        for pre in self.pre_g.get(node, []):
            self.g[pre].discard(node)
            if not self.g[pre]:
                self.remove_node(pre)


if __name__ == '__main__':
    solution = Solution()
    print(solution.eventualSafeNodes([[0, 6, 7, 9], [], [], [], [2, 6, 8], [7, 9], [7, 8, 9], [], [6, 9], [7]]))
