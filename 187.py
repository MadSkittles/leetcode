class Solution:
    def findRepeatedDnaSequences(self, s):
        exists, repeat = set(), set()
        for i in range(0, len(s) - 9):
            if s[i:i + 10] in exists:
                repeat.add(s[i:i + 10])
            exists.add(s[i:i + 10])
        return list(repeat)
