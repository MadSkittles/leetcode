class Solution(object):
    def circularArrayLoop(self, nums):
        l = len(nums)
        for i in range(len(nums)):
            if not nums[i]:
                continue
            j, k = i, (l + i + nums[i]) % l
            while nums[j] * nums[k] > 0 and nums[(l + k + nums[k]) % l] * nums[i] > 0:
                if j == k:
                    if j == (l + j + nums[j]) % l:
                        break
                    return True
                j = (l + j + nums[j]) % l
                k = (l + (l + k + nums[k]) % l + nums[(l + k + nums[k]) % l]) % l
            j = i
            while nums[j] * nums[i] > 0:
                nums[j], j = 0, (l + j + nums[j]) % l
        return False
