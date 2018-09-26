class Solution:
    def convertToTitle(self, n):
        s = ""
        while n:
            s = chr(ord("A") + (n - 1) % 26) + s
            n = (n - 1) // 26
        return s


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(701))
