class Solution:
    def findWords(self, board, words):
        self.board, trie = board, {}
        for word in words:
            p = trie
            for c in word:
                p = p.setdefault(c, {})
            p['#'] = '#'
        self.grid = [[False] * len(board[0]) for _ in board]
        self.res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.f(i, j, trie, '')
        return list(self.res)

    def f(self, x, y, trie, s):
        if '#' in trie:
            self.res.add(s)
        if not (0 <= x < len(self.board) and 0 <= y < len(self.board[0])):
            return
        if not self.grid[x][y] and self.board[x][y] in trie:
            self.grid[x][y] = True
            self.f(x + 1, y, trie[self.board[x][y]], s + self.board[x][y])
            self.f(x - 1, y, trie[self.board[x][y]], s + self.board[x][y])
            self.f(x, y + 1, trie[self.board[x][y]], s + self.board[x][y])
            self.f(x, y - 1, trie[self.board[x][y]], s + self.board[x][y])
            self.grid[x][y] = False


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(
        [["b"], ["a"], ["b"], ["b"], ["a"]],
        ["baa", "abba", "baab", "aba"]))
