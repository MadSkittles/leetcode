# Container With Most Water

class Solution:
	def maxArea(self, height):
		left, right = 0, len(height) - 1
		max_area = -1
		while left < right:
			area = (right - left) * min(height[left], height[right])
			if area > max_area:
				max_area = area
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		return max_area


if __name__ == '__main__':
	solution = Solution()
	print(solution.maxArea([2, 3, 4, 5, 17, 18, 6]))

