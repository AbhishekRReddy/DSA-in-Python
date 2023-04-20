'''
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
'''

class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        nums = [int(s) for s in num]
        nums.sort()
        new1 = nums[0] * 10 + nums[2]
        new2 = nums[1] * 10 + nums[3]
        return new1 + new2 