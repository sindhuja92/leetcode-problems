"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order."""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        neg = 0
        for x in range(len(A)):
            if A[x] < 0:
                neg += 1 
        
        new_list = []
        
        i = neg-1
        j = neg
        
        while i>=0 and j<len(A):
            if A[i]**2 < A[j]**2:
                new_list.append(A[i]**2)
                i = i - 1
            else:
                new_list.append(A[j]**2)
                j = j + 1
        
        
        
        while i>=0:
            new_list.append(A[i]**2)
            i = i - 1
        while j<len(A):
            new_list.append(A[j]**2)
            j = j + 1
            
        return new_list
