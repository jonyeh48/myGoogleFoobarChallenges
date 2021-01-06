def solution(total_lambs):
    #Finding min henchmen paid uses power of 2 sequence from 2^0
    min_seq = []
    min_sum = 0
    min_counter = 0
    while min_sum <= total_lambs:
        min_temp = 2**min_counter
        if min_sum + min_temp <= total_lambs:
            min_seq.append(min_temp)
            min_sum = sum(min_seq)
            min_counter += 1
        else:
            break
    #Finding max henchmen paid uses Fibonacci sequence from 1
    max_seq = [1,1]
    max_sum = sum(max_seq)
    while max_sum <= total_lambs:
        max_temp = max_seq[len(max_seq)-2] + max_seq[len(max_seq)-1]
        if max_sum + max_temp <= total_lambs:
            max_seq.append(max_temp)
            max_sum = sum(max_seq)
        else:
            break
    diff = len(max_seq) - len(min_seq)
    return diff
