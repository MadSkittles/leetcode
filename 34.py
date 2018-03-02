class Solution:
    def searchRange(self, nums, target):
        start, end = 0, len(nums) - 1
        head = tail = None
        while start <= end:
            mid = int((start + end) / 2)
            if mid > 0:
                if nums[mid - 1] < target:
                    if nums[mid] == target:
                        head = mid
                        break
                    elif nums[mid] > target:
                        return [-1, -1]
                    else:
                        start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] == target:
                    head = mid
                    break
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    return [-1, -1]

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if mid < len(nums) - 1:
                if nums[mid + 1] > target:
                    if nums[mid] == target:
                        tail = mid
                        break
                    elif nums[mid] < target:
                        return [-1, -1]
                    else:
                        end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] == target:
                    tail = mid
                    break
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    return [-1, -1]

        if head is None and tail is None:
            return [-1, -1]
        elif head is None:
            return [tail, tail]
        elif tail is None:
            return [head, head]
        else:
            return [head, tail]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([], 2))
    print(solution.searchRange([1, 2], 2))
    print(solution.searchRange([2, 2], 2))
    print(solution.searchRange([1, 2, 2], 2))
    print(solution.searchRange([2, 2, 3], 2))
    print(solution.searchRange([1, 2, 2, 3], 2))
    print(solution.searchRange([2, 3, 4], 2))
    print(solution.searchRange([2, 3, 4], 4))
    print(solution.searchRange([2, 3, 4], 5))
