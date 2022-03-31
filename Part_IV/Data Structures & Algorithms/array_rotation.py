def rotate(l, n):
    return l[-n % len(l):] + l[:-n % len(l)]

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))



