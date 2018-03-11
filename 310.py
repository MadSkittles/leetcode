class Solution:
    def findMinHeightTrees(self, n, edges):
        graph, leaf, non_leaf = {}, set(), set()
        for start, end in edges:
            graph.setdefault(start, []).append(end)
            graph.setdefault(end, []).append(start)
        start_leaf_node = None
        for n in graph:
            if len(graph[n]) == 1:
                start_leaf_node = n if start_leaf_node is None else start_leaf_node
                leaf.add(n)
            else:
                non_leaf.add(n)
        from queue import Queue
        visited, path_to_node = {start_leaf_node}, []
        q = Queue()
        q.put((start_leaf_node, (start_leaf_node,)))
        while not q.empty():
            start, cur_path = q.get()
            flag = 0
            for end in graph[start]:
                if end not in visited:
                    q.put((end, (*cur_path, end)))
                    visited.add(end)
                    flag += 1
            if not flag:
                path_to_node.append(cur_path)
        print(path_to_node)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
