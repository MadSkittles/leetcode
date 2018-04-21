class Solution:
    def findOrder(self, numCourses, prerequisites):
        from queue import Queue
        graph, pre_graph = {}, {}
        for course, pre_course in prerequisites:
            graph.setdefault(pre_course, set()).add(course)
            pre_graph.setdefault(course, set()).add(pre_course)

        res, q = [], Queue()
        list(map(lambda x: q.put(x), [c for c in range(numCourses) if c not in pre_graph]))
        while not q.empty():
            c = q.get()
            res.append(c)
            for next_c in graph.get(c, []):
                pre_graph[next_c].remove(c)
                if not pre_graph[next_c]:
                    q.put(next_c)
        return res if len(res) == numCourses else []
