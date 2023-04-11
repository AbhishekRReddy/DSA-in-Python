'''
https://www.codingninjas.com/codestudio/problems/frog-jump_3621012
'''
def frogJump(n: int, heights: list[int]) -> int:
    # Write your code here.
    if n == 1:
        dp[n] = 0
        return 0
    if n in dp:
        return dp[n]
    left = frogJump(n-1,heights) + abs(heights[n-1]-heights[n-2])
    if n > 2:
        right = frogJump(n-2,heights) + abs(heights[n-1]-heights[n-3])
        dp[n] = min(left, right)
        return dp[n]
    dp[n] = left
    return dp[n]

def frogJump_tab(n,heights):
    prev1 = 0
    prev2 = 0
    for i in range(1, n):
        one_jump = prev1 + abs(heights[i] - heights[i-1])
        two_jump = float('inf')
        if i>1:
            two_jump = prev2 + abs(heights[i]- heights[i-2])
        curri = min(one_jump,two_jump)
        prev2 = prev1
        prev1 = curri
    return curri





print(frogJump_tab(4,[10,20,30,10]))
