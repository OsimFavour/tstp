"""Write a program that tests a string for balanced parantheses.
"""

# the key to solving this problem is to use stack
 
def balanced_paren(expression):
    stack = []

    for c in expression:
        if c == "(" :
            stack.append(c)
        elif c == ")" :
            if len(stack) < 1:
                return False
            stack.pop()
            if len(stack) == 0:
                return True
            return False

print(balanced_paren("(hello)"))           

print(balanced_paren(")"))


