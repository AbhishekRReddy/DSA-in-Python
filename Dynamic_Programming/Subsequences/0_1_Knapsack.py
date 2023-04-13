'''
https://www.codingninjas.com/codestudio/problems/0-1-knapsack_1072980?leftPanelTab=1
'''
'''
Trying out all ways with recursion
'''
def knapsk(values,weights,n,w):
    if n == 0:
        if w >= weights[n]:
            return values[n]
        return 0
    not_pick = knapsk(values,weights,n-1,w)
    pick = float('-inf')
    if w >= weights[n]:
        pick =values[n] + knapsk(values,weights,n-1,w-weights[n])
    return max(pick,not_pick)

'''
DP with Memoization
'''
def knapsk(values,weights,n,w,dp):
    if n == 0:
        if w >= weights[n]:
            return values[n]
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    not_pick = knapsk(values,weights,n-1,w,dp)
    pick = float('-inf')
    if w >= weights[n]:
        pick =values[n] + knapsk(values,weights,n-1,w-weights[n],dp)
    dp[n][w] = max(pick,not_pick)
    return dp[n][w]

def maxProfit(values, weights, n, w):
    dp = [ [-1]*(w+1) for i in range(n)] 
    return knapsk(values,weights,n-1,w,dp)


