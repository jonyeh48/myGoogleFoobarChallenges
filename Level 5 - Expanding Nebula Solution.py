#This was extremely hard. Cellular Automaton is no joke. Solution heavily influenced by Jinzhou Zhang's (lotabout)'s solution. https://gist.github.com/lotabout/891621ae8a01d8e512afd4b5254516b4
def create(c1,c2,bit_length):
    w = c1 & ~(1<<bit_length)
    x = c2 & ~(1<<bit_length)
    y = c1 >> 1
    z = c2 >> 1
    return (w&~x&~y&~z) | (~w&x&~y&~z) | (~w&~x&y&~z) | (~w&~x&~y&z)
from collections import defaultdict
def construct_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            creation = create(i,j,n)
            if creation in nums:
                mapping[(creation, i)].add(j)
    return mapping
import numpy as np
def solution(g):
    g = list(np.transpose(g))
    nrows = len(g)
    ncols = len(g[0])
    #turn map into numbers
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = construct_map(ncols, nums)

    prev_pic = {i: 1 for i in range(1<<(ncols+1))}
    for row in nums:
        row2 = defaultdict(int)
        for c1 in prev_pic:
            for c2 in mapping[(row, c1)]:
                row2[c2] += prev_pic[c1]
        prev_pic = row2
    ans = sum(prev_pic.values())
    return ans
