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