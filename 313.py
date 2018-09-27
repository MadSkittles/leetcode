import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly, index, heap = [1], [0] * len(primes), [(v, i) for i, v in enumerate(primes)]
        heapq.heapify(heap)
        while n > 1:
            umin, umin_pos = heapq.heappop(heap)
            if umin > ugly[-1]:
                ugly.append(umin)
                n -= 1
            index[umin_pos] += 1
            heapq.heappush(heap, (primes[umin_pos] * ugly[index[umin_pos]], umin_pos))
        return ugly[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.nthSuperUglyNumber(100000, [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]))
