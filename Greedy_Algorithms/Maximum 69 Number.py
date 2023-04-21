'''
https://leetcode.com/problems/maximum-69-number/description/
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [int(s) for s in str(num)]
        for i,n in enumerate(nums):
            if n == 6:
                nums[i] = 9
                break
        x = ''.join(list(map(str,nums)))
        return int(x)