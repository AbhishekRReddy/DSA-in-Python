'''
https://www.codingninjas.com/codestudio/problems/0-1-knapsack_1072980?leftPanelTab=1
'''
'''
Trying out all ways with recursion
'''
def knapsk(values,weights,n,w):
    if n == 0:
        if w >= weights[n]:
            return values[n]
        return 0
    not_pick = knapsk(values,weights,n-1,w)
    pick = float('-inf')
    if w >= weights[n]:
        pick =values[n] + knapsk(values,weights,n-1,w-weights[n])
    return max(pick,not_pick)

