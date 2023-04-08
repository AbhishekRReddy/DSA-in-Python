'''
https://www.codingninjas.com/codestudio/problems/frog-jump_3621012
'''
def frogJump(n: int, heights: list[int]) -> int:
    # Write your code here.
    if n == 1:
        return 0
    left = frogJump(n-1,heights) + abs(heights[n-1]-heights[n-2])
    if n > 2:
        right = frogJump(n-2,heights) + abs(heights[n-1]-heights[n-3])
        return min(left, right)
    return left

print(frogJump(4,[10,20,30,10]))