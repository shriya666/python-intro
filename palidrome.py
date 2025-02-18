def is_palindrome(str):
    str=str.lower()
    str=str.split()
    str="".join(str)
    left_point= 0
    right_point= len(str)- 1
    while left_point <= right_point:
        if str[left_point] != str[right_point]:
            return False
        left_point+=1
        right_point-=1
    return True

print(is_palindrome("Murder for a jar of red rum"))

