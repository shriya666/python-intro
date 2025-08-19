import random
# This one uses factorial with a NON recurrsive method
def factorial(number):
    distance= number- 1
    answer = number
    for i in range (1, distance+1):
        answer *= i
    return answer
#This one is recurssive because it calls its function again 
def fac2(number):
    if number==1:
        return 1
    return number * fac2(number - 1)

print(fac2(7))


def addinglist(list):
    answer = ""
    for i in list:
        answer= answer+i
    return answer 
#the type function checks what type of input it is (str or int) in order for the list to return something that make sense 
def addinglist2(list, type):
    if list==[]:
        if type is int:
            return 0
        else:
            return ""
    else:
        answer=list[0]+ addinglist2(list[1:], type) 
    return answer

print(addinglist2([3, 6, 9], int))