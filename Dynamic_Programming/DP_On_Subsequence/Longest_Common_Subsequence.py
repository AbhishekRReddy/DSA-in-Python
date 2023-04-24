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