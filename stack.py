#!/usr/bin/python3
"""
implements a stack using Queues.
"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.i = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.i.append(x)
        self.len += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element
        """
        n = self.len
        while n > 1:
            self.i.append(self.i.pop(0))
            n -= 1
        self.len -= 1
        return self.i.pop(0)

    def top(self):
        """
        Get the top element.
        """
        n = self.len
        while n > 1:
            self.i.append(self.i.pop(0))
            n -= 1
        ret = self.i.pop(0)
        self.i.append(ret)
        return ret

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return self.len == 0
