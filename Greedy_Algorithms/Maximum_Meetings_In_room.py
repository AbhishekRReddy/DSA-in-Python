'''
https://practice.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
'''
class Solution:
    def maxMeetings(self, N : int, S : list[int], F : list[int]) -> list[int]:
        # code here
        time = [(i+1,S[i],F[i]) for i in range(N)]
        time.sort(key = lambda x : x[2])
        meetings = []
        meetings.append(time[0][0])
        end = time[0][2]
        for i in range(1,N):
            if time[i][1] > end:
                meetings.append(time[i][0])
                end = time[i][2]
        meetings.sort()
        return meetings