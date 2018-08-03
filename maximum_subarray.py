#!/usr/bin/python3
"""
finds the contiguous subarray which has the largest 
sum and returns it's sum.
"""
class Solution(object):
    def maxSubArray(self,nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
