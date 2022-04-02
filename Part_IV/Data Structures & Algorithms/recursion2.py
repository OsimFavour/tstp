"""Given a non-negative integer num repeatedly add all 
   it's digits until the results has only one digits
"""
def add_digits(number):
    """
    :param number: int
    :return: Single digit int
    """
    number = str(number)
    if len(number) == 1:
        return int(number)
    the_sum = 0
    for c in number:
        the_sum += int(c)
        return add_digits(the_sum)

print(add_digits(99)) 