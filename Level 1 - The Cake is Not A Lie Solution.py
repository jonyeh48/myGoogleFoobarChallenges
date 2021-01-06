def solution(s):
    import numpy as np
    slices = list(s)
    #Count number of elements in list and find the divisor
    divisors = []
    for i in range(2,len(slices) + 1):
        if len(slices) % i == 0:
            divisors.append(i)
    #identifying sequence pattern
    counter = [0 for i in divisors]
    seq_pos = slices
    for j in range(len(divisors)):
        res = True
        while res == True:
            seq_matrix = []
            for i in range(divisors[j]):
                seq_temp = [seq_pos[k] for k in range(len(seq_pos)*i//divisors[j],len(seq_pos)*(i+1)//divisors[j])]
                seq_matrix.append(seq_temp)
            res = all(seq_hope == seq_matrix[0] for seq_hope in seq_matrix)
            if res == True:
                counter[j] += 1
                seq_pos = seq_matrix[0]
            else:
                break
    #determining maximum number of slices
    cuts_per_div = [divisors[i] ** counter[i] for i in range(len(divisors))]
    slice_count = np.prod(cuts_per_div)
    return slice_count
