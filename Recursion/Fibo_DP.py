def fib(n,dp):
    if n <= 1:
        dp[n] = n
        return dp[n]
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1,dp) + fib(n-2, dp)
    return dp[n]

def fibo_tab(n,dp):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def febo_space(n):
    prev1 = 0
    prev2 = 1
    for i in range(2,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr



n = 7
dp = [-1]*(n+1)
print(febo_space(7))
