"""Optimized bubble sort
"""

def bubble_sort(array):
    for i in range(len(array)):                     # loop through each element of array
        swapped = False                             # keep track of swapping
        for j in range(0, len(array) -i -1):        # loop to compare array elements[j]
            if array[j] > array[j + 1]:             # compare two adjacent elements, change > to < to sort in descending order
                temp = array[j]
                array[j] = array[j + 1]             # Swapping occurs if elements are not in the intended order
                array[j + 1] = temp
                swapped = True
            if not swapped:                         # No swapping means the arrayis already sorted
                break                               # So no need for futher comparison

data = [-2, 45, 0, 11, -9]
bubble_sort(data)

print("Sorted Array in Ascending Order: ")
print(data)