#!/bin/python3

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countDict = {}
        for index in range(len(nums)): 
            if (countDict.get(nums[index])) : 
                countDict[nums[index]] = countDict[nums[index]] + 1
            else: 
                countDict[nums[index]] = 1
        for key, value in countDict.items():
            if value == 1:
                 return key