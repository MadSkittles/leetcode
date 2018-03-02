class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in result:
                result[key] = []
            result[key].append(s)

        return list(result.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
