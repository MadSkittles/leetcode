class Solution:
    def topKFrequent(self, words, k):
        import heapq
        from collections import Counter
        return [k for _, k in heapq.nsmallest(k, [(-v, k) for k, v in Counter(words).items()])]