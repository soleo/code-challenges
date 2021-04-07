#!/bin/python3

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        totalNumberCount = len(nums)
        uniqNumberCount = 0
        for currentIndex in reversed(range(totalNumberCount)):
            previousIndex = currentIndex - 1
            if currentIndex > 0 and nums[currentIndex] == nums[previousIndex]:
                del nums[currentIndex]
            else:    
                uniqNumberCount = uniqNumberCount + 1
        return uniqNumberCount