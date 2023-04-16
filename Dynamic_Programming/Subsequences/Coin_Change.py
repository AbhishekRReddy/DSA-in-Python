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

