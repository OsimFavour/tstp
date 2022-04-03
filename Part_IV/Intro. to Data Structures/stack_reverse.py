from stack import Stack 

my_string = "Hello"
stack = Stack()

for c in my_string:
    stack.push(c)

new_string = ""
for i in range(len(stack.items)):
    new_string += stack.pop()
print(new_string)