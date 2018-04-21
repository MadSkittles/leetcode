class Solution:
    def isBipartite(self, graph):
        self.graph = graph
        self.flag = [0] * len(graph)
        return self.f(0)

    def f(self, index):
        if index >= len(self.graph):
            return True
        if (self.flag[index] > 0 and any(self.flag[i] > 0 for i in self.graph[index])) or (self.flag[index] < 0 and any(self.flag[i] < 0 for i in self.graph[index])):
            return False
        if self.flag[index] > 0 or any(self.flag[i] < 0 for i in self.graph[index]):
            self.flag[index] += 1
            for i in self.graph[index]:
                self.flag[i] -= 1
            res = self.f(index + 1)
            self.flag[index] -= 1
            for i in self.graph[index]:
                self.flag[i] += 1
        elif self.flag[index] < 0 or any(self.flag[i] < 0 for i in self.graph[index]):
            self.flag[index] -= 1
            for i in self.graph[index]:
                self.flag[i] += 1
            res = self.f(index + 1)
            self.flag[index] += 1
            for i in self.graph[index]:
                self.flag[i] -= 1
        else:
            self.flag[index] += 1
            for i in self.graph[index]:
                self.flag[i] -= 1
            res = self.f(index + 1)
            self.flag[index] -= 1
            for i in self.graph[index]:
                self.flag[i] += 1
            if not res:
                self.flag[index] -= 1
                for i in self.graph[index]:
                    self.flag[i] += 1
                res = self.f(index + 1)
                self.flag[index] += 1
                for i in self.graph[index]:
                    self.flag[i] -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
