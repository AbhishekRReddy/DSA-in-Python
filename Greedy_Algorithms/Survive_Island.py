'''
https://practice.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1
'''
class Solution:
    def minimumDays(self, S, N, M):
        # code here
        sunday = S//7
        buy_days = S-sunday
        ans = 0
        stock = S*M
        if stock % N == 0:
            ans = stock // N
        else:
            ans = stock // N + 1
        if ans <= buy_days:
            return ans
        else:
            return -1