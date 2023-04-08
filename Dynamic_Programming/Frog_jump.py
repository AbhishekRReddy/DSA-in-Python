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

dp = {}
print(frogJump(4,[10,20,30,10]))
print(dp)