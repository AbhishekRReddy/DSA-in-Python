'''
Problem Description
 
 

N light bulbs are connected by a wire.

Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.


Problem Constraints
0 <= N <= 5e5
0 <= A[i] <= 1


Input Format
The first and the only argument contains an integer array A, of size N.


Output Format
Return an integer representing the minimum number of switches required.

'''



class Solution:
	# @param A : list of integers
	# @return an integer
    def bulbs(self, A):
        cost = 0
        for b in A:
#If the cost is even, then the current bit is same as original.
#So we are keeping as-is.
#If its odd, then it needs to be swapped and further it should be checked
#for whether it needs be swapped or not.
            if cost % 2 == 0:
                b = b
            else:
                b = 1 - b
            
            if b == 0:
                cost += 1
            else:
                continue
        return cost 
