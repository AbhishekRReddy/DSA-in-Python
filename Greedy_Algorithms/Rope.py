'''
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
'''

import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        if n == 1:
            return 0
        heapq.heapify(arr)
        cost = 0
        global_cost = 0
        while len(arr) > 2:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            cost = a + b
            global_cost += cost
            heapq.heappush(arr,cost)
        return arr[0] + arr[1] + global_cost

