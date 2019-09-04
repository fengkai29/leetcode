from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        """
        if self.queue:
            return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return not bool(self.queue)