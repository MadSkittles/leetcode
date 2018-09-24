class Solution:
    def shiftingLetters(self, S, shifts):
        from itertools import accumulate

        s = [*accumulate(shifts[::-1], lambda x, y: (x + y) % 26)]
        return "".join(chr((ord(c) - 97 + s[len(s) - i - 1]) % 26 + 97) for i, c in enumerate(S))


if __name__ == "__main__":
    solution = Solution()
    print(solution.shiftingLetters('abc', [3, 5, 9]))
    print(
        solution.shiftingLetters(
            "mkgfzkkuxownxvfvxasy",
            [
                505870226,
                437526072,
                266740649,
                224336793,
                532917782,
                311122363,
                567754492,
                595798950,
                81520022,
                684110326,
                137742843,
                275267355,
                856903962,
                148291585,
                919054234,
                467541837,
                622939912,
                116899933,
                983296461,
                536563513,
            ],
        )
    )
