class Solution:
    def productExceptSelf(self, nums):
        product, reverse_product = 1, 1
        products, reverse_products = [], []
        for i in range(len(nums)):
            product *= nums[i]
            products.append(product)
            reverse_product *= nums[len(nums) - 1 - i]
            reverse_products.append(reverse_product)
        reverse_products = reverse_products[::-1]
        for i in range(len(nums)):
            nums[i] = (products[i - 1] if i > 0 else 1) * (reverse_products[i + 1] if i + 1 < len(nums) else 1)
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([]))
