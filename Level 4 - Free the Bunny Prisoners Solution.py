#This solution is a modified version of the solution on the Dalao's World github page, linked here: https://vitaminac.github.io/Google-Foobar-Free-the-Bunny-Prisoners/
#This was my first time using the itertools package and the enumerate function
from itertools import combinations
def solution(num_buns, num_required):
    key_dist = [[] for i in range(num_buns)]
    key_copies = num_buns - num_required + 1
    for key, buns in enumerate(combinations(range(num_buns),key_copies)):
        for bun in buns:
            key_dist[bun].append(key)
    return key_dist
