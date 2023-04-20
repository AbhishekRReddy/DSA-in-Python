'''
https://leetcode.com/problems/fibonacci-number/description/
'''

'''
With memoization
'''
def fibo(n,dp):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    return fibo(n-1,dp) + fibo(n-2,dp)



class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        return fibo(n,dp)

'''
DP with tabulation
'''

class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 0
        if n == 0:
            return dp[0]
        dp[1] = 1
        if n == 1:
            return dp[1]
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
'''
Tabualtion with space optimization
'''
class Solution:
    def fib(self, n: int) -> int:
        prev2 = 0
        if n == 0:
            return prev2
        prev1 = 1
        if n == 1:
            return prev1
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr