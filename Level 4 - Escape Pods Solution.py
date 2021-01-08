#This solution is derived from Suraj Shetiya's solution on his blog, linked here: https://surajshetiya.github.io/Google-foobar/
#It uses Dinic's Algorithm to solve the problem
def bfs(matrix, source, destination):#does Breadth-first Search algorithm
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    queue = [source]
    while len(queue) > 0:
        top = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[top][i][1] - matrix[top][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    # Get route
                    visited[destination] = top
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    # Get flow value and update augmented graph
                    temp = 1
                    total = float("inf")
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        cur = path[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        if entry[1] < 0: # Already augmented need to flip
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][cur]
                        if entry[1] <= 0: # Already augmented need to flip
                            entry[1] -= total
                        else:
                            entry[0] += total
                        cur = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = top
                    queue.append(i)
    return False
def solution(entrances, exits, path):
    max_buns = sum(list(map(sum, path)))
    inc = []
    for i in range(len(path)):
        inc.append([])
        for j in range(len(path[i])):
            inc[i].append([0,path[i][j]])
        inc[i].append([0,0])
        if i in exits:
            inc[i].append([0, max_buns])
        else:
            inc[i].append([0,0])
    inc.append([])
    inc.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            inc[-2].append([0,max_buns])
        else:
            inc[-2].append([0,0])
        inc[-1].append([0,0])
    while bfs(inc,len(inc)-2, len(inc)-1):
        pass
    tot_buns = 0
    for i in range(len(inc)):
        tot_buns += inc[-2][i][0]
    return tot_buns

#Here is what I wrote, which was able to pass the first 3 out of 4 test cases. Turns out I just got lucky on those 3.
import numpy as np
def solution(entrances, exits, path):
    num_rooms = len(path)
    room_plot = [0 for i in range(num_rooms)]#This will count how many bunnies will be in each room based on how many can fit in corridor
    #entrance elements don't matter because don't really care about those rooms
    min_buns = 2000000 #at most 2000000 bunnies will fit at a time
    min_rmsplvl = 50 #at most 50 rooms connected by corridors
    path_t = np.array(path).T
    for i in range(len(path_t)):
        for j in range(len(path_t[i])):
            room_plot[i] += path_t[i][j]
            temp_minbuns = room_plot[i]
        temp_minrpl = np.count_nonzero(path[i])
        if temp_minbuns < min_buns and temp_minbuns > 0 or i == len(entrances):
            min_buns = temp_minbuns
        if temp_minrpl < min_rmsplvl and temp_minrpl > 0 or i == len(entrances):
            min_rmsplvl = temp_minrpl
    min_bunnies = min_buns * min_rmsplvl
    return min_bunnies
