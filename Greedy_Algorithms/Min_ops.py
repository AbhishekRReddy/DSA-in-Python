'''
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
'''
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        global_count = 0
        local = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                local = nums[i-1] - nums[i] + 1
                nums[i] += local
                global_count += local 
        return global_count
