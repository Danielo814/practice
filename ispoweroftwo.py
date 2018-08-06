#!/usr/bin/python3
"""
determines if an integer is a power of two
"""
class Solution:
    def isPowerOfTwo(self, n)
        if n < 1:
            return False
        while not n % 2:
            n /= 2
        return n == 1
