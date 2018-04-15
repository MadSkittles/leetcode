class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        from collections import Counter
        licensePlate = Counter(filter(lambda c: c.isalpha(), licensePlate.lower()))
        res, min_length = [], float('inf')
        for word in words:
            w = Counter(word)
            if all([w[k] >= licensePlate[k] for k in licensePlate]) and len(word) < min_length:
                res.append(word)
                min_length = len(word)
        for word in res:
            if len(word) == min_length:
                return word
        return None