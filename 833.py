class Solution:
    def findReplaceString(self, S, indexes: list, sources, targets):
        if not indexes:
            return S
        indexes = sorted(zip(indexes, sources, targets))
        res = S[:indexes[0][0]]
        for i, rep in enumerate(indexes):
            index, w, t = rep
            if S[index:index + len(w)] == w:
                res += t
                res += S[index + len(w):indexes[i + 1][0] if i + 1 < len(indexes) else len(S)]
            else:
                res += S[index:indexes[i + 1][0] if i + 1 < len(indexes) else len(S)]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findReplaceString("imidcxiiqjwpvvcocjtskshvmqjnlhsqtezqttmoxuskbmujej",
                                     [35, 6, 22, 40, 17, 19, 12, 2, 42, 4, 8, 45, 14, 29, 47, 24],
                                     ["qtt", "ii", "hv", "xu", "jt", "sk", "vv", "id", "skb", "cx", "qjw", "mu", "co", "hsqtez", "jej", "mqjnl"],
                                     ["idl", "vo", "yl", "pg", "efp", "vqi", "s", "wb", "mw", "gmt", "rkqc", "kdx", "o", "vamwgpn", "pl", "xyvz"]))
