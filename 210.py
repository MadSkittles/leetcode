# 课程的依赖序列就是拓扑排序的序列

class Solution:
    def findOrder(self, numCourses, prerequisites):
        from queue import Queue
        graph, pre_graph = {}, {}
        for course, pre_course in prerequisites:
            graph.setdefault(course, set()).add(pre_course)
            pre_graph.setdefault(pre_course, set()).add(course)

        cnt, res, q = 0, [], Queue()
        list(map(lambda x: q.put(x), [c for c in range(numCourses) if c not in pre_graph]))
        while not q.empty():
            node = q.get()
            cnt += 1
            res.append(node)
            for pre in graph.get(node, set()):
                pre_graph[pre].remove(node)
                if not len(pre_graph[pre]):
                    q.put(pre)
        return res[::-1] if cnt == numCourses else []
