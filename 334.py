class Solution:
    def increasingTriplet(self, nums):
        one = two = float('inf')
        for n in nums:
            if n <= one:
                one = n
            elif n <= two:
                two = n
            else:
                return True
        return False
