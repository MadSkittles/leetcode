class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        index = [0] * len(primes)
        umins = primes[::]
        while n > 1:
            umin, umin_pos = float('inf'), 0
            for i, v in enumerate(umins):
                if v < umin:
                    umin = v
                    umin_pos = i
            index[umin_pos] += 1
            if umin > ugly[-1]:
                ugly.append(umin)
                n -= 1
            umins[umin_pos] = primes[umin_pos] * ugly[index[umin_pos]]
        return ugly[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nthSuperUglyNumber(100000,
                                      [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139,
                                       157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]))
