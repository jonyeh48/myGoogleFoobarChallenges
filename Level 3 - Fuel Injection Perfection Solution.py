#This solution was inspired by Chris from the finxter blog, linked here: https://blog.finxter.com/googles-foobar/#Level_3_Challenge_2
def solution(n):
    n_int = int(n)
    oper = 0
    while n_int > 1:
        if n_int & 1 == 1:
            if n_int % 4 == 1 or n_int == 3:
                n_int -= 1
            else:
                n_int += 1
        else:
            n_int = n_int >> 1
        oper += 1
    return oper
#Below is what I developed prior to searching this up.
#I basically had the gist of the concept, but the part about n_int == 3 didn't occur to me. 
#Instead of forcing it to subtract by 1 when n_int == 3, it was going through the standard procedure of "looking ahead to see if it is divisible by 4"
#which resulted in adding an extra operation to the minimum
#Original Code (This is wrong!)
def solution(n):
    n_int = int(n)
    oper = 0
    while n_int > 1:
        if n_int % 2 == 0:
            n_int /= 2
        else:
            dnu = (n_int + 1)/2
            dnd = (n_int - 1)/2
            if dnu % 2 == 0:
                n_int += 1
            else:
                n_int -= 1
        oper += 1
    retrn oper
