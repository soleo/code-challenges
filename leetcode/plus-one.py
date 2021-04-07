#!/bin/python3

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] = digits[len(digits)-1] + 1
        for i in reversed(range(len(digits))):
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i-1] = digits[i-1] + 1          
        return digits