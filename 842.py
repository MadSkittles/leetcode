class Solution:
    def splitIntoFibonacci(self, S):
        N = len(S)
        for i in range(1, N // 2 + 1):
            for j in range(i + 1, N):
                first, second, index = S[:i], S[i:j], j
                res = [first, second]
                while index < N:
                    if (first[0] == '0' and first != '0') or (second[0] == '0' and second != '0'):
                        break
                    if N - index < max(len(first), len(second)):
                        break
                    m = int(first) + int(second)
                    if m >= 2 ** 31:
                        break
                    n = str(m)
                    if S[index:index + len(n)] == n:
                        first, second, index = second, n, index + len(n)
                        res.append(n)
                    else:
                        break
                if index >= N:
                    return [*map(int, res)]
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
