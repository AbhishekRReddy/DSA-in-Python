'''
https://www.codingninjas.com/codestudio/problems/ways-to-make-coin-change_630471
'''
def way(d,value, index):
    if value == 0:
        return 1 
    if value < 0 or index < 0:
        return 0
    pick = 0
    if d[index]<=value:
        pick = way(d,value-d[index],index)
    not_pick = way(d,value,index-1)
    return pick + not_pick


def countWaysToMakeChange(denominations, value) :
	# Your code goes here
    return way(denominations,value, len(denominations)-1)

'''
DP with memoization
'''
def way(d,value, index,dp):
    if value == 0:
        return 1 
    if value < 0 or index < 0:
        return 0
    if dp[value][index] != -1:
        return dp[value][index]
    pick = 0
    if d[index]<=value:
        pick = way(d,value-d[index],index,dp)
    not_pick = way(d,value,index-1,dp)
    dp[value][index] = pick + not_pick
    return dp[value][index]

def countWaysToMakeChange(denominations, value) :
	# Your code goes here
    dp = [ [-1]*len(denominations) for _ in range(value+1)]

    return way(denominations,value, len(denominations)-1,dp)

'''
DP with Tabulation
'''
def countWaysToMakeChange(denominations, value) :
	# Your code goes here
    dp = [ [-1]*len(denominations) for _ in range(value+1)]
    for i in range(len(denominations)):
        dp[0][i] = 1
    for m in range(1, value+1):
        for n in range(len(denominations)):
            pick = 0
            not_pick = 0
            if n > 0:
                not_pick = dp[m][n-1]
            if denominations[n] <= m:
                pick = dp[m-denominations[n]][n]
            dp[m][n] = not_pick + pick
    
    return dp[value][len(denominations)-1]
