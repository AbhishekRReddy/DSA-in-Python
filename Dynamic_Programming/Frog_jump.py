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
    dp = [0]*n
    dp[0] = 0 #Base Case
    for i in range(1, n):
        one_jump = dp[i-1] + abs(heights[i] - heights[i-1])
        two_jump = float('inf')
        if i > 1:
            two_jump = dp[i-2] + abs(heights[i]- heights[i-2])
        dp[i] = min(one_jump,two_jump)
    return dp[n-1]





print(frogJump_tab(4,[10,20,30,10]))
