from stack import Stack as s 

my_string = "Hello"
stack = s()

for c in my_string:
    stack.push(c)

new_string = ""
for i in range(len(stack.items)):
    new_string += stack.pop()
print(new_string)