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


'''
DP with the Tabulation
'''

def maxProfit(values, weights, n, w):
    dp = [ [-1]*(w+1) for i in range(n)]
    for x in range(w+1):
        if x >= weights[0]:
            dp[0][x] = values[0]
        else:
            dp[0][x] = 0
    for i in range(1,n):
        for j in range(w+1):
            not_pick = dp[i-1][j]
            pick = float('-inf')
            if j >= weights[i]:
                pick = values[i] + dp[i-1][j-weights[i]]
            dp[i][j] = max(not_pick,pick)
    return dp[n-1][w]

'''
DP with tabulation with Space Optimization
'''
def maxProfit(values, weights, n, w):
    dp = [0]*(w+1)
    for x in range(w+1):
        if x >= weights[0]:
            dp[x] = values[0]
        else:
            dp[x] = 0
    for i in range(1,n):
        curr_row = [0] * (w+1)
        for j in range(w+1):
            not_pick = dp[j]
            pick = float('-inf')
            if j >= weights[i]:
                pick = values[i] + dp[j-weights[i]]
            curr_row[j] = max(not_pick,pick)
        dp = curr_row
    return dp[w]


