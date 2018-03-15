class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        return (C - A) * (D - B) + (G - E) * (H - F) - ((right - left) if right > left else 0) * (
            (top - bottom) if top > bottom else 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
