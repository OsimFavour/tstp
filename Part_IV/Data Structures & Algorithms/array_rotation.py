"""rotate an array of n elements to the right by k steps 
"""

def rotate(l, n):
    # return l[-n % len(l):] + l[:-n % len(l)]
    return  l[-n:] #+ l[:-n]

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))


# they still give the same output [5, 6, 7, 1, 2, 3, 4]




