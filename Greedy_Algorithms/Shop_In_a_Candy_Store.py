'''
https://practice.geeksforgeeks.org/problems/shop-in-candy-store1145/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
'''
class Solution:
    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        for_max = candies[:]
        min = 0
        max = 0
        while len(for_max)>0:
            min += for_max.pop(0)
            for _ in range(K):
                if len(for_max)>0:
                    for_max.pop()
        while len(candies)>0:
            max += candies.pop()
            for _ in range(K):
                if len(candies)>0:
                    candies.pop(0)
        return min,max