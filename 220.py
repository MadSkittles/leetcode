# 将所有数字划分成若干个桶，每个桶的长度为t，所以每个桶内的数字相差不会超过t。如果当前桶还不存在，则与相邻的桶比较。

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}
        for i, v in enumerate(nums):
            bucketNum, offset = (v // t, 1) if t else (v, 0)

            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                for n, index in buckets.get(idx, []):
                    if abs(n - nums[i]) <= t and abs(index - i) <= k:
                        return True

            buckets.setdefault(bucketNum, []).append((v, i))
        return False


if __name__ == '__main__':
    solution = Solution()
