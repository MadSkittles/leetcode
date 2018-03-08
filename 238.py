class Solution:
    def productExceptSelf(self, nums):
        product, products = 1, []
        for i in range(len(nums)):
            product *= nums[i]
            products.append(product)
        product, pre = 1, 1
        for i in range(len(nums) - 1, -1, -1):
            product *= pre
            pre = nums[i]
            nums[i] = product * (products[i - 1] if i > 0 else 1)
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([]))
