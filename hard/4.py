"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List
from math import ceil

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merged_sorted_list = sorted(nums1)

        if (len(merged_sorted_list) == 1):
            return merged_sorted_list[0]

        if (len(merged_sorted_list) % 2 == 0):
            return (merged_sorted_list[(len(merged_sorted_list)//2) - 1] + merged_sorted_list[len(merged_sorted_list)//2]) / 2
        
        return merged_sorted_list[ceil(len(merged_sorted_list)/2) - 1]
        

solution = Solution()

print(solution.findMedianSortedArrays([1,3], [2]))   # Expected 2
print(solution.findMedianSortedArrays([1,2], [3,4])) # Expected 2.5
