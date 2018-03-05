class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if not endWord in wordList:
            return 0
        visited_nodes = {beginWord}
        self.wordList = set(wordList + [beginWord])

        nodes, length = [beginWord], 1
        while nodes:
            next_nodes = []
            for cur_node in nodes:
                path = self.generate_next_nodes(cur_node)
                for next_n in path:
                    if next_n == endWord:
                        return length + 1
                    if next_n not in visited_nodes:
                        visited_nodes.add(next_n)
                        next_nodes.append(next_n)
            nodes = next_nodes
            length += 1
        return 0

    def generate_next_nodes(self, s):
        res = []
        for i in range(len(s)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                ss = s[:i] + c + s[i + 1:]
                if ss in self.wordList:
                    res.append(ss)
        return res


if __name__ == '__main__':
    solution = Solution()
