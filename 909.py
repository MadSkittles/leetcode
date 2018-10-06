from queue import Queue


class Solution:
    def snakesAndLadders(self, board):
        graph, dest = [None], len(board) ** 2
        for i in range(-1, -len(board) - 1, -1):
            graph.extend(board[i] if i & 1 else board[i][::-1])
        q, visited = Queue(), {1: 0}
        q.put((1, 0))
        while not q.empty():
            pos, move = q.get()
            if pos >= dest:
                continue
            for i in range(pos + 1, pos + 7):
                j = min(i, dest)
                next = j if graph[j] == -1 else graph[j]
                if visited.get(next, float("inf")) > move + 1:
                    visited[next] = move + 1
                    q.put((next, move + 1))
        return visited.get(dest, -1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
