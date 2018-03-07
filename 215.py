class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        return heap[0]


if __name__ == '__main__':
    solution = Solution()
    from random import shuffle

    l = list(range(200))
    shuffle(l)
    print(solution.findKthLargest(l, 5))
