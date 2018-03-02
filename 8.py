# String to Integer (atoi)

class Solution:
	def myAtoi(self, str):
		str = str.strip()
		base = 1
		if str.startswith('-') or str.startswith('+'):
			base = -1 if str.startswith('-') else 1
			str = str[1:]
		
		str = str.lstrip('0')
		result = 0
		print(base)
		for i in range(len(str)):
			if not str[i].isdigit():
				break
			digit = int(str[i])
			if i == 9:
				if result > 214748364 or (result == 214748364 and digit >= (7
																														if base > 0 else 8)):
					return 2147483647 if base > 0 else -2147483648
			if i > 9:
				return 2147483647 if base > 0 else -2147483648

			result = result * 10 + digit

		return base * result


if __name__ == '__main__':
	solution = Solution()
	#print(solution.myAtoi('214748364899'))
	print(solution.myAtoi('-2147483647'))
