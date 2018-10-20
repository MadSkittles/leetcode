from collections import Counter


class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        diff, cnt, max_num = [], Counter(), 0
        for c1, c2 in zip(A, B):
            if c1 != c2:
                diff.append((c1, c2))
            else:
                cnt[c1] += 1
                max_num = max(max_num, cnt[c1])
        return (len(diff) == 2 and diff[0] == diff[1][::-1]) or (len(diff) == 0 and max_num >= 2)


if __name__ == "__main__":
    solution = Solution()
    from random import randint

    rand = [chr(97 + randint(0, 25)) for _ in range(20000)]
    A = "".join(rand)
    a, b = randint(0, 19999), randint(0, 19999)
    rand[a], rand[b] = rand[b], rand[a]
    B = "".join(rand)
    print(solution.buddyStrings(A, B))

