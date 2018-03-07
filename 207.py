class Solution:
    def canFinish(self, numCourses, prerequisites):
        from queue import Queue
        graph, pre_graph = {}, {}
        for course, pre_course in prerequisites:
            graph.setdefault(course, set()).add(pre_course)
            pre_graph.setdefault(pre_course, set()).add(course)

        cnt, q = 0, Queue()
        list(map(lambda x: q.put(x), [c for c in range(numCourses) if c not in pre_graph]))
        while not q.empty():
            node = q.get()
            cnt += 1
            for pre in graph.get(node, set()):
                pre_graph[pre].remove(node)
                if not len(pre_graph[pre]):
                    q.put(pre)
        return cnt == numCourses
