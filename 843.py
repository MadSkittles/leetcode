class Master:
    def guess(self, word):
        """
        :type word: str
        :rtype int
        """


class Solution:
    def findSecretWord(self, wordlist, master):
        word, *wordlist = wordlist
        space = set(wordlist)
        test = master.guess(word)
        while test != 6:
            space = {*filter(lambda x: sum(x[i] == word[i] for i in range(6)) == test, space)}
            word = space.pop()
            test = master.guess(word)
