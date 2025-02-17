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

# #even numbers from a list
# def even_numbers(nums):
#     newlist1=[]
#     # divisible= nums % 2
#     for i in nums:
#         if i % 2==0:
#             newlist1.append(i)

#     return newlist1
#         # if divisible== 0:
#         #     return nums
# print(even_numbers([1, 2, 3, 4, 564, 8, 9]))

    #even numbers are divisible by two so you have to check if the number is divisible by 2
    # for i in nums:
    #     if i/2:
    #         return 

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


