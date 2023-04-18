'''
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
'''
class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        time = [(start[i],end[i]) for i in range(len(start))]
        time.sort(key = lambda x : x[1])
        end = time[0][1]
        count = 1
        for i in range(1,len(start)):
            if time[i][0] > end:
                count += 1
                end = time[i][1]
        return count