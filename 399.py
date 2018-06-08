class Solution:
    def calcEquation(self, equations, values, queries):
        division_map, graph = {}, {}
        for i in range(len(equations)):
            a, b = equations[i]
            division_map[(a, b)] = values[i]
            division_map[(a, a)] = 1.0
            graph.setdefault(a, set()).add(b)
            division_map[(b, a)] = 1 / values[i]
            division_map[(b, b)] = 1.0
            graph.setdefault(b, set()).add(a)

        from queue import Queue

        elements, start_node = set(graph.keys()), []
        while elements:
            start = elements.pop()
            start_node.append(start)
            q = Queue()
            q.put((start, 1))
            while not q.empty():
                f, l = q.get()
                for t in graph[f]:
                    if t in elements:
                        q.put((t, l * division_map[(f, t)]))
                        elements.remove(t)
                        division_map[(start, t)] = l * division_map[(f, t)]
        res = []
        for a, b in queries:
            for s in start_node:
                if (s, a) in division_map and (s, b) in division_map:
                    res.append(division_map[(s, b)] / division_map[(s, a)])
                    break
            else:
                res.append(-1.0)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.calcEquation(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )
