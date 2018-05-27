class Solution:
    def canVisitAllRooms(self, rooms):
        from queue import Queue
        q, visited = Queue(), {0}
        q.put(0)
        while not q.empty():
            c = q.get()
            for n in rooms[c]:
                if n not in visited:
                    q.put(n)
                    visited.add(n)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canVisitAllRooms([[1], [2], [3], []]))
    print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
