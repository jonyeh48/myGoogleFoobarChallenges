#This solution was taken straight from the GeeksForGeeks website linked here: https://www.geeksforgeeks.org/total-number-of-different-staircase-that-can-made-from-n-boxes/
def solution(n):
    tracker = [[0 for num_bricks in range(n+5)] for num_steps in range(n+5)]
    #Base case
    #matrix says tracker[number of bricks][number of steps] = number of possible stairs configuration
    tracker[3][2] = 1
    tracker[4][2] = 1
    for i in range(5,n+1):
        for j in range(2,i+1):
            #When step = 2
            if j == 2:
                tracker[i][j] = tracker[i-j][j] + 1
            #When step > 2
            else:
                tracker[i][j] = tracker[i-j][j] + tracker[i-j][j-1]
    #Count total number of staircases from all steps
    total_choices = 0
    for i in range(1,n+1):
        total_choices += tracker[n][i]
    return total_choices
