'''
https://leetcode.com/problems/shortest-common-supersequence/description/
'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [ [-1] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 0
        for i in range(m+1):
            dp[i][0] = 0
        
        for x in range(1,m+1):
            for y in range(1,n+1):
                if str1[x-1] == str2[y-1]:
                    dp[x][y] = 1 + dp[x-1][y-1]
                else:
                    way1 = dp[x-1][y]
                    way2 = dp[x][y-1]
                    dp[x][y] = max(way1,way2)
        ans = ''
        while m > 0 and n > 0:
            if str1[m-1] == str2[n-1]:
                ans += str1[m-1]
                m -= 1
                n -= 1 
            elif dp[m-1][n] > dp[m][n-1]:
                ans += str1[m-1]
                m -= 1
            else:
                ans += str2[n-1]
                n -= 1
        while m > 0:
            ans += str1[m-1]
            m -= 1
        while n > 0:
            ans += str2[n-1]
            n -= 1
        return ans[::-1]



