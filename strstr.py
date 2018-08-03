#!/usr/bin/python3
"""
program to return index of first occurance
of "needle" in "haystack"
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        finds index of first occurance of needle in haystack
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
