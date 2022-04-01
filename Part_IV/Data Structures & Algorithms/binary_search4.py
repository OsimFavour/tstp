"""Binary search using recursive method
"""

def binary_search(array, x, low, high):

    # repeat until the pointers low and high meet each other 
    if high >= low :
        mid = low + (high - low)//2

        # if found at mid, then retun it
        if array[mid] == x:
            return mid

        # search the left half
        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        # search the right half
        else:
             binary_search(array, x, mid+1, high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binary_search(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")