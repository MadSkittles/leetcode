class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        answers = []
        word_list = wordList
        if len(word_list) == 0: return answers
        if len(beginWord) != len(endWord): return answers
        if len(endWord) != len(word_list[0]): return answers
        if endWord not in word_list: return answers

        word_len = len(endWord)

        i_differ_list = []
        for i in range(word_len):
            i_differ_map = {}
            for word in word_list:
                substr = word[:i] + word[i + 1:]
                if substr not in i_differ_map:
                    i_differ_map[substr] = []
                i_differ_map[substr].append(word)
            i_differ_list.append(i_differ_map)

        visited = set()
        parents = {}

        def do_bfs(curr_words):
            for curr_word in curr_words:
                visited.add(curr_word)

            found = False
            next_words = set()
            while curr_words:
                curr_word = curr_words.pop()
                for i in range(word_len):
                    substr = curr_word[:i] + curr_word[i + 1:]
                    for next_word in i_differ_list[i].get(substr, []):
                        if next_word == endWord:
                            found = True
                        if next_word not in visited:
                            if next_word not in parents:
                                parents[next_word] = []
                            parents[next_word].append(curr_word)
                            next_words.add(next_word)

            if not found and next_words:
                found = do_bfs(next_words)

            return found

        def do_dfs(prefix):
            tail = prefix[-1]
            if tail == beginWord:
                answers.append(prefix[::-1])
            else:
                for parent in parents[tail]:
                    do_dfs(prefix + [parent])

        if do_bfs({beginWord}):
            do_dfs([endWord])

        return answers
