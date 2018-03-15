class Solution:
    def wiggleMaxLength(self, nums):
        length = [1] if nums else [0]
        reverse_length = [1] if nums else [0]
        for i in range(1, len(nums)):
            length.append(max([1 + length[j] for j in range(i - 1, -1, -1) if
                               ((length[j] & 1 and nums[i] > nums[j]) or (not length[j] & 1 and nums[i] < nums[j]))] + [
                                  1]))
            reverse_length.append(max([1 + reverse_length[j] for j in range(i - 1, -1, -1) if
                                       ((reverse_length[j] & 1 and nums[i] < nums[j]) or (
                                               not reverse_length[j] & 1 and nums[i] > nums[j]))] + [1]))
        return max(length + reverse_length)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleMaxLength([3, 3, 3, 2, 5]))
