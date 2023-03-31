#Given N number of activities with start and end times. We need to select the maximum number of activities
#that can be performed by a single person ,assuming that a person can only work on a 
#single activity at a time.
#Selecting the the minimum end time greedily
activities = [['A1', 0, 6],
              ['B1', 3 , 4],
              ['A3', 1, 2],
              ['A4', 5, 8],
              ['A5', 5, 7],
              ['A6', 8, 9]
]
def print_max_activities(activities):
    activities.sort(key =lambda x:x[2]) #This is key to algoritms tht greedily select the minimum finish time.
    i = 0
    first_act = activities[i][0]
    print(first_act)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j
print_max_activities(activities)
    
