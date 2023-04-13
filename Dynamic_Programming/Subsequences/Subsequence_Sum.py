'''
https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=0
'''
#Below is trying out all possible subsequence with recursion and it results in TLE

def subek(n,k,arr):
    if k == 0:
        return True
    if n == 0:
        return k == arr[0]
    not_take = subek(n-1,k,arr)
    take = False
    if k >= arr[n]:
        take = subek(n-1,k-arr[n],arr)
    return take or not_take