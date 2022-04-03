def binary_search(number_list, number):
    """Logarithmic binary search algorithm.
       :param number_list: List of ordered integers.
       :param number: Integer to search for in the passed in list.
       :return: True if the number is found, otherwise False.
    """
    first = 0
    last = len(number_list)-1
    number_found = False

    while first <= last and not number_found:
        middle = (first + last)//2
        if number_list[middle] == number:
            number_found = True
        else:
            if  number < number_list[middle]:
                last = middle - 1 
            else:
                first = middle + 1

    return number_found
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
print(result)