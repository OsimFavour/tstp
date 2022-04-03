def Binary_search(num, desired_value, left, right):
    while left <= right:
        mid = (left + right)//2
        if desired_value == num[mid]:
            return num[mid]                                 #changed mid to num[mid] to get the middle indexed value in num
        elif desired_value > num[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
num = [12, 15, 19, 20, 22, 29, 38, 41, 44, 90, 106, 397, 399, 635]
desired_value = 41
result = Binary_search(num, desired_value, 0, len(num)-1)
# if result != -1:
#     print("Number found at " + str(result), "th index")
# else:
#     print("Number not found")
print(result)