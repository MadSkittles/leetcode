class Solution:
    def decodeAtIndex(self, S, K):
        s = 0
        for i, c in enumerate(S):
            if c.isalpha():
                t = s + 1
                last_c = c
            else:
                t = s * int(c)
            if t > K:
                pos = i
                K = (K - 1) % s + 1
                break
            elif t == K:
                return last_c
            s = t
        return self.decodeAtIndex(S[:pos], K)


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeAtIndex("leet2code3", 4))
    print(solution.decodeAtIndex("ha22", 5))
    print(solution.decodeAtIndex("a2345678999999999999999", 1))
