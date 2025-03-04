#already done: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, circlearea, reversefullname
# import random
# import string
# def better_print(str):
#     print(str+"!")

# better_print("xwv")

# def number_counter(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum
# print(number_counter([2, 3, 5]))

# def reverse(str):
#     words=""
#     for i in range(len(str)-1, -1, -1):
#         words+=str[i]
#     return words
# print(reverse("desserts"))


# def factorial(num):
#     product= 1
#     for i in range(1, num+1):
#         product*= i
#     return product
# print(factorial(4))

# def unique(lst):
#     newlist= []
#     for i in lst:
#         if i not in newlist:
#             newlist.append(i)
#     return newlist
# print(unique([1,2,2,3]))


# def even_numbers(nums):
#     newlist1=[]
#     for i in nums:
#         if i % 2==0:
#             newlist1.append(i)

#     return newlist1
# print(even_numbers([1, 2, 3, 4, 564, 8, 9]))

# def is_palindrome(str):
#     left= 0
#     right= len(str) -1
#     while right >= left:
#         if not str[left]== str[right]:
#             return False
#         left += 1
#         right -=1
#     return True

# print(is_palindrome("racecar"))


# def in_range():
#     num= random.randint(1,20)
#     print(num)
#     if num>= 1 and num<=12:
#         return True
#     else: 
#         return False
# print(in_range())

# def upper_and_lower(str):
#     char1=0
#     char2=0
#     for i in str:
#         if i.isupper():
#             char1+=1
#         else:
#             char2+=1
#     return char1, char2
# print(upper_and_lower("Anuya"))

# def is_prime(num):
#     num_root= int(num**0.5)
#     for i in range(2, num_root+1):
#         if num%i == 0:
#             return False
#         else:
#             return True
# print(is_prime(34))

# def is_perfect(nummy):
#     divisors=[]
#     for i in range(1, nummy+1):
#         if nummy%i ==0:
#            divisors.append(i)
#     sum=0
#     for i in divisors:
#         sum+=i
#     if sum-nummy==nummy and sum==nummy*2:
#         return True
#     else:
#         return False
# print(is_perfect(300))

# def square_nums():
#     squares= []
#     for i in range(1, 31):
#         squares.append(i**2)
#     return squares
# print(square_nums())

# def squares(num):
#     square= num**2
#     return square
# print(squares(9))

# def is_panagram(str):
#     letters= set(string.ascii_lowercase)
#     input_set= set(str.lower())
#     return letters.issubset(input_set)

# print(is_panagram("Sphinx of black quartz, judge my vow"))

# def area_circumference(d):
#     r= d/2
#     area= r**2*3.14
#     circ= d*3.14
#     return area, circ 
# print(area_circumference(1))

# def reverse_order(str):
#     a= str
#     str1= (a.split())
#     return str1[1], str1[0]
# print(reverse_order("Shriya Rajurkar"))

# def reverse_order_again(str):
#     str2= str.split("-")
#     b= str2[ : :-1]
#     return b
# print(reverse_order_again("green-blue-gold-pink-purple-turquoise"))

# def alpha(str):
#     str3= str.split("-")
#     str4=sorted(str3)
#     str5="-".join(str4)
#     return str5
# print(alpha("green-black-blue-white-gray"))


def last_letter(str):
    empty_array= ""
    for i in range(len(str)-1,-1,-1):
       empty_array+=str[i]
    return empty_array[i]+ empty_array[-1:]

print(last_letter("shriya"))
    