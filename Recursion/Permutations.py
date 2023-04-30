'''
https://leetcode.com/problems/permutations/description/
'''

def f(nums, lenx, local_sol, freq, global_sol):
    if len(local_sol) == lenx:
        global_sol.append(local_sol[:])
        return
    for i in range(lenx):
        if not freq[i]:
            local_sol.append(nums[i])
            freq[i] = True
            f(nums,lenx,local_sol,freq,global_sol)
            local_sol.remove(nums[i])
            freq[i] = False 

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        global_sol =[]
        local_sol = []
        lenx = len(nums)
        freq = {i:False for i in range(lenx)}
        f(nums,lenx,local_sol,freq,global_sol)
        return global_sol