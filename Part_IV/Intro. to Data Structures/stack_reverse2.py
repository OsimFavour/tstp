def reverse(s: str):
    stack = []
    reversed_string = ""
    for ch in s:
        stack.append(ch)
    while len(stack):
        reversed_string += stack.pop()
    return reversed_string

print(reverse("abc"))