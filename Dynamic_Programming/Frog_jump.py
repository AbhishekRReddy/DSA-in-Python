from os import *
from sys import *
from collections import *
from math import *
from typing import *


def jump(n,h,dp):
    if n == 0:
        dp[0] = 0
        return 0      
    if dp[n] != -1:
        return dp[n]
    take = jump(n-1,h,dp) + abs(h[n] - h[n-1])
    not_take = float('inf')
    if n > 1:
        not_take = jump(n-2,h,dp) + abs(h[n] - h[n-2])
    dp[n] = min(take, not_take)
    return dp[n]

    
def frogJump(n: int, heights: List[int]) -> int:
    prev1 = 0
    prev2 = 0
    h = heights
    for i in range(1,n):
        take = prev1 + abs(h[i] - h[i-1])
        not_take = float('inf')
        if i > 1:
            not_take = prev2 + abs(h[i] - h[i-2])
        prev2 = prev1
        prev1 = min(take,not_take)
    return prev1

    

