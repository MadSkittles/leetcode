class Solution(object):
    def validUtf8(self, data):
        if len(data) == 0:
            return True
        i = 0
        while i < len(data):
            if data[i] < 128:
                i += 1
            elif data[i] >= 192 and data[i] < 224 and len(data) - i >= 2:
                if data[i + 1] >= 128 and data[i + 1] < 192:
                    i += 2
                else:
                    return False
            elif data[i] >= 224 and data[i] < 240 and len(data) - i >= 3:
                if data[i + 1] >= 128 and data[i + 1] < 192 and data[i + 2] >= 128 and data[i + 2] < 192:
                    i += 3
                else:
                    return False
            elif data[i] >= 240 and data[i] < 248 and len(data) - i >= 4:
                if data[i + 1] >= 128 and data[i + 1] < 192 and data[i + 2] >= 128 and data[i + 2] < 192 and data[
                    i + 3] >= 128 and data[i + 3] < 192:
                    i += 4
                else:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.validUtf8([39, 89, 227, 83, 132, 95, 10, 0]))
