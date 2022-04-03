"""Bubble sort is a sorting algorithm that compares two adjacent elements and swaps
   them until they are in the intended order
"""
def bubble_sort(array):

    # loop to access each array element
    for i in range(len(array)):
    
        # loop to compare each array element
        for j in range(0, len(array) -i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended number
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [-2, 45, 0, 11, -9]
bubble_sort(data)
print("Sorted array in Ascending order:")
print(data)