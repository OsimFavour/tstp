def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict
        else:
            a_dict[n] = index
    print(a_dict)
            
# two_sum([-1, 2, 3, 4, 7])

target = 5
two_sum([-1, 2, 3, 4, 7], target)  
# the code isn't running, when I have data I'll check it out