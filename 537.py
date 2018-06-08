class Solution:
    def complexNumberMultiply(self, a, b):
        import re

        a_index, b_index = (
            re.search("\d[+-]", a).start() + 1,
            re.search("\d[+-]", b).start() + 1,
        )
        complex_a, complex_b = (
            (int(a[:a_index]), int(a[a_index + 1 : -1])),
            (int(b[:b_index]), int(b[b_index + 1 : -1])),
        )
        return (
            str(complex_a[0] * complex_b[0] - complex_a[1] * complex_b[1])
            + "+"
            + str(complex_a[0] * complex_b[1] + complex_a[1] * complex_b[0])
            + "i"
        )


if __name__ == "__main__":
    solution = Solution()
    print(solution.complexNumberMultiply("1+1i", "1+1i"))
    print(solution.complexNumberMultiply("1+-1i", "1+-1i"))
