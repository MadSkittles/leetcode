class Solution:
    def repeatedStringMatch(self, A, B):
        s = A * (len(B) // len(A))
        for n in range(len(B) // len(A), len(B) // len(A) + 3):
            if B in s:
                return n
            s += A
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedStringMatch("abcd", "cdabcdab"))
