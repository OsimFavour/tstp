class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise IndexError("Cannot pop from empty stack")
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        return True