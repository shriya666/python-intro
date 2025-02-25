import random
def better_print(str):
    print(str+"!")

better_print("xwv")

def number_counter(lst):
    sum = 0
    for i in lst:
        sum += i

    return sum
print(number_counter([2, 3, 5]))

def reverse(str):
    words=""
    for i in range(len(str)-1, -1, -1):
        words+=str[i]
    return words
print(reverse("desserts"))


def factorial(num):
    product= 1
    for i in range(1, num+1):
        product*= i
    return product
print(factorial(4))

def unique(lst):
    newlist= []
    for i in lst:
        if i not in newlist:
            newlist.append(i)
    return newlist
print(unique([1,2,2,3]))


def even_numbers(nums):
    newlist1=[]
    # divisible= nums % 2
    for i in nums:
        if i % 2==0:
            newlist1.append(i)

    return newlist1
        # if divisible== 0:
        #     return nums
print(even_numbers([1, 2, 3, 4, 564, 8, 9]))

def is_palindrome(str):
    left= 0
    right= len(str) -1
    while right >= left:
        if not str[left]== str[right]:
            return False
        left += 1
        right -=1
    return True

print(is_palindrome("racecar"))


def in_range():
    num= random.randint(1,20)
    print(num)
    if num>= 1 and num<=12:
        return True
    else: 
        return False
print(in_range())

def upper_and_lower(str):
    char1=0
    char2=0
    for i in str:
        if i.isupper():
            char1+=1
        else:
            char2+=1
    return char1, char2
print(upper_and_lower("Anuya"))

def is_prime(num):
    num_root= int(num**0.5)
    for i in range(2, num_root+1):
        if num%i == 0:
            return False
        else:
            return True
print(is_prime(34))

def is_perfect(nummy):
    divisors=[]
    for i in range(1, nummy+1):
        if nummy%i ==0:
           divisors.append(i)
    sum=0
    for i in divisors:
        sum+=i
    if sum-nummy==nummy and sum==nummy*2:
        return True
    else:
        return False
    
print(is_perfect(300))








