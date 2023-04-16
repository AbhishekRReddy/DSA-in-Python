'''
https://www.codingninjas.com/codestudio/problems/ways-to-make-coin-change_630471
'''
def way(d,value, index):
    if value == 0:
        return 1 
    if value < 0:
        return 0
    pick = way(d,value-d[index],index)
    not_pick = 0
    if index > 0:
        not_pick = way(d,value,index-1)
    return pick + not_pick


def countWaysToMakeChange(denominations, value) :
	# Your code goes here
    return way(denominations,value, len(denominations)-1)