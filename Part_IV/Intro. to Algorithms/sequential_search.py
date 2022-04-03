"""Sequential search is a simple search algorithm that checks each number in 
   the list one by one to see if it matches the number it is looking for
"""

def sequential_search(number_list, number):
    """
    :param number_list: List of integers.
    :param_number: Integer to look for.
    :return: True if the number is found, otherwise false.
    """
    found = False
    for i in number_list:
        if i == number:
            found = True
            break
    return found

print (sequential_search(range(0, 100), 2))
print (sequential_search(range(0, 100), 202))

# Output == True
# Output == False
