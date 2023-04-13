'''
https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=0
'''
#Below is trying out all possible subsequence with recursion and it results in TLE

def subek(n,k,arr):
    if k == 0:
        return True
    if n == 0:
        return k == arr[0]
    not_take = subek(n-1,k,arr)
    take = False
    if k >= arr[n]:
        take = subek(n-1,k-arr[n],arr)
    return take or not_take

'''
DP with Memoization
'''
def subek(n,k,arr,dp):
    if k == 0:
        return True
    if n == 0:
        return k == arr[0]
    if dp[n][k] != -1:
        return dp[n][k]
    not_take = subek(n-1,k,arr,dp)
    take = False
    if k >= arr[n]:
        take = subek(n-1,k-arr[n],arr,dp)
    dp[n][k] = take or not_take
    return dp[n][k]

def subsetSumToK(n, k, arr):
    dp = [ [-1]*(k+1) for _ in range(n)]
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return subek(n-1,k,arr,dp)
    
'''
DP with Tabulation
'''
def subsetSumToK(n, k, arr):
    dp = [ [-1]*(k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    for j in range(1,k+1):
        dp[0][j] = j == arr[0]
    for x in range(1,n):
        for y in range(1,k+1):
            not_take = dp[x-1][y]
            take = False
            if y >= arr[x]:
                take = dp[x-1][y-arr[x]]
            dp[x][y] = take or not_take
    return dp[n-1][k]

'''
DP Tabulation with Space Optimization
'''

def subsetSumToK(n, k, arr):
    dp = [-1]*(k+1)
    dp[0] = True
    for j in range(1,k+1):
        dp[j] = j == arr[0]
    for x in range(1,n):
        temp = [0]*(k+1)
        temp[0] = True
        for y in range(1,k+1):
            not_take = dp[y]
            take = False
            if y >= arr[x]:
                take = dp[y-arr[x]]
            temp[y] = take or not_take
        dp = temp
    return dp[k]