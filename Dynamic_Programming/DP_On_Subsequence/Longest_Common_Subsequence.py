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