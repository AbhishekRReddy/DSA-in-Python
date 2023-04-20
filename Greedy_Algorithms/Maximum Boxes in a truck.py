'''
https://leetcode.com/problems/maximum-units-on-a-truck/description/
'''
def truck(goods, truck):
    goods.sort(key = lambda x : x[1],reverse = True)
    print(goods)
    currw = 0
    cost = 0 
    i = 0
    while i < len(goods) and truck > 0:
        if goods[i][0] <= truck:
            cost += goods[i][0] * goods[i][1]
            truck -= goods[i][0]
            i += 1
        else:
            cost += truck * goods[i][1]
            break
    return cost


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        return truck(boxTypes,truckSize)