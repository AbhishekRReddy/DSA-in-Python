'''
https://leetcode.com/problems/longest-common-subsequence/
'''
#Recursion solution, trying out all ways

def lstr(strx,stry,xind,yind):
    if xind < 0 or yind < 0:
        return 0
    if strx[xind] == stry[yind]:
        return 1 + lstr(strx,stry,xind-1,yind-1)
    return max(lstr(strx,stry,xind,yind-1), lstr(strx,stry,xind-1,yind))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return lstr(text1,text2,len(text1)-1,len(text2)-1)

'''
Memoization
'''
def lstr(strx,stry,xind,yind,dp):
    if xind < 0 or yind < 0:
        return 0
    if dp[xind][yind] != -1:
        return dp[xind][yind]
    if strx[xind] == stry[yind]:
        dp[xind][yind] = 1 + lstr(strx,stry,xind-1,yind-1,dp)
        return dp[xind][yind]
    dp[xind][yind] = max(lstr(strx,stry,xind,yind-1,dp), lstr(strx,stry,xind-1,yind,dp))
    return dp[xind][yind]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n= len(text2)
        dp = [ [-1]*n for _ in range(m) ]
        return lstr(text1,text2,m-1,n-1,dp)

'''
DP with Tabualation - array is left shifted to accomodate the base cases
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n= len(text2) + 1 #For shifitng purpose
        dp = [ [-1]*n for _ in range(m) ]
        for x in range(n):
            dp[0][x] = 0
        for y in range(m):
            dp[y][0] = 0

        for x in range(1,m):
            for y in range(1,n):
                if text1[x-1] == text2[y-1]:
                    dp[x][y] = 1 + dp[x-1][y-1]
                    continue
                non_match1 = dp[x][y-1]
                non_match2 = dp[x-1][y]
                dp[x][y] = max(non_match1, non_match2) 
        return dp[m-1][n-1]