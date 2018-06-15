class Solution:
    def loudAndRich(self, richer, quiet):
        graph = {}
        for a, b in richer:
            graph.setdefault(b, []).append(a)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def f(n):
            return min(
                [f(c) for c in graph.get(n, [])] + [(quiet[n], n)], key=lambda x: x[0]
            )

        return [f(i)[1] for i in range(len(quiet))]


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.loudAndRich(
            [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
            [3, 2, 5, 4, 6, 1, 7, 0],
        )
    )
