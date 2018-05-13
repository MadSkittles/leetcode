class Solution:
    def sumOfDistancesInTree(self, N, edges):
        size, up, down, graph = [1] * N, [0] * N, [0] * N, {}
        for i, j in edges:
            graph.setdefault(i, []).append(j)
            graph.setdefault(j, []).append(i)

        def post_order(parent, i):
            for j in graph.get(i, []):
                if j != parent:
                    post_order(i, j)
                    size[i] += size[j]
                    down[i] += down[j] + size[j]

        def pre_order(parent, i):
            if parent is not None:
                up[i] = up[parent] + down[parent] - down[i] - size[i] + N - size[i]
            for j in graph.get(i, []):
                if j != parent:
                    pre_order(i, j)

        post_order(None, 0)
        pre_order(None, 0)
        return [up[i] + down[i] for i in range(N)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfDistancesInTree(N=1, edges=[]))
