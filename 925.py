class Solution:
    def isLongPressedName(self, name, typed):
        name, typed = self.helper(name), self.helper(typed)
        return len(name) == len(typed) and all(name[i][0] == typed[i][0] and name[i][1] <= typed[i][1] for i in range(len(name)))

    def helper(self, name):
        res = []
        if not name:
            return res
        p, cnt = name[0], 1
        name += "#"
        for c in name:
            if c == p:
                cnt += 1
            else:
                res.append((p, cnt))
                p, cnt = c, 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.isLongPressedName("alex", "aaleex"))
    print(solution.isLongPressedName("saeed", "ssaaedd"))
    print(solution.isLongPressedName("leelee", "lleeelee"))
    print(solution.isLongPressedName("laiden", "laiden"))
