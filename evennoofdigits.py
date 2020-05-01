# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total_count = 0
        for i in nums:
            count = 0
            while i > 0:
                i = i // 10
                count = count + 1
            if count % 2 == 0:
                total_count = total_count + 1
        return total_count
