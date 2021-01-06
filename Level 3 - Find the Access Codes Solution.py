#This code was derived from n3a9's java solution, which is at https://github.com/n3a9/google-foobar/blob/master/Level%203/find_the_access_codes/solution.java
#Embedded are my interpretation of how the code works
def solution(l):
    count = 0
    if len(l) < 3:
        count = 0
    else:
        for i in range(1,len(l)-1):#start with the middle number of the first 3 numbers in the list
            counta = 0 #first number in the triplet [a,b,c]
            countc = 0 #last number in the triplet [a,b,c]
            for j in range(0,i):
                if l[i] % l[j] == 0: #if b is cleanly divisible by a then count it
                    counta += 1
            for k in range(i+1,len(l)):
                if l[k] % l[i] == 0: #if c is cleanly divisible by b then count it
                    countc += 1
            count += counta * countc #Multiplying these counts indicates the number of possible triplet codes for b
    return count
