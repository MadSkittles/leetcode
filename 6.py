# ZigZag Conversion 

class Solution:
	def convert(self, s, numRows):
		if numRows == 1:
			return s
		step = numRows * 2 - 2
		result = ''
		for i in range(numRows):
			j = i
			short_step = None if i == 0 or i == numRows - 1 else 2 * (numRows - i - 1)
			while j < len(s):
				result += s[j]
				result += s[j +
																short_step] if short_step and j + short_step < len(s) else ''
				j += step
		return result


print(Solution().convert('A', 1))

