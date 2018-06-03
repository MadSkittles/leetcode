class Solution:
    def slidingPuzzle(self, board):
        start = ''.join(map(str, board[0] + board[1]))
        if start == '123450':
            return 0
        from queue import Queue
        q, visited = Queue(), {start}
        q.put((start, start.index('0'), 0))
        while not q.empty():
            s, index, step = q.get()
            next = []
            if index != 0 and index != 3:
                next.append((s[:index - 1] + s[index] + s[index - 1] + s[index + 1:], index - 1, step + 1))
            if index != 2 and index != 5:
                next.append((s[:index] + s[index + 1] + s[index] + s[index + 2:], index + 1, step + 1))
            if index + 3 < 6:
                next.append((s[:index] + s[index + 3] + s[index + 1:index + 3] + s[index] + s[index + 4:], index + 3, step + 1))
            if index - 3 >= 0:
                next.append((s[:index - 3] + s[index] + s[index - 2:index] + s[index - 3] + s[index + 1:], index - 3, step + 1))
            for n in next:
                if n[0] == '123450':
                    return n[2]
                if not n[0] in visited:
                    visited.add(n[0])
                    q.put(n)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
