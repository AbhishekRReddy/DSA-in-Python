'''
https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
'''

class Solution:

    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        i = 0
        j = M-1
        minx = float('inf')
        while j < len(A):
            diff = A[j] - A[i]
            minx = min(minx, diff)
            i += 1
            j += 1
        return minx