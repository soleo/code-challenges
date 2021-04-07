#!/bin/python3

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == k:
            return None
        elif n < k: 
            k = k % n
        
        last_k_nums = nums[-k:]
        for i in reversed(range(n)):
            if i >= k: 
                nums[i] = nums[i-k]
            else:
                nums[i] = last_k_nums[i]
   