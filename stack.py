"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):  # constructor
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):  # lets us to use print statement to inspect the stack
        return str(self.items)


# if this stack class is imported, we don't want code in here to be running
# if __name__ == "__main__": - checks if this is the main file I'm running, and only runs code if that's the case
if __name__ == "__main__":
    s = Stack()  # capital letter for class construction
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)

    s.push(7)
    s.push(13)
    s.push(23)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)
    print(s.size())
