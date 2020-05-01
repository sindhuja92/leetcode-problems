"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000 """

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
               count += 1
            else:   
                if count > final_count:
                    count, final_count = final_count, count
                count = 0
        if count > final_count:
            return count
        return final_count
