class Solution:
    def compareVersion(self, version1, version2):
        version1, version2 = self.strip_zero([int(i) for i in version1.split('.')]), self.strip_zero([int(i) for i in version2.split('.')])
        index = 0
        while index < len(version1) and index < len(version2):
            if version1[index] != version2[index]:
                return 1 if version1[index] > version2[index] else -1
            index += 1
        if not index == len(version1) == len(version2):
            return 1 if index < len(version1) else -1
        return 0

    def strip_zero(self, s: list):
        index = len(s) - 1
        while s[index] == 0 and index > 0:
            index -= 1
        return s[:index + 1]