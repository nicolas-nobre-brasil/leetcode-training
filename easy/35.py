"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""
from typing import List

class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        for num in nums:
            if num > target:
                return nums.index(num)

        return len(nums)

solution = Solution()

print(solution.searchInsert([1,3,5,6], 5)) # Expected 2
print(solution.searchInsert([1,3,5,6], 2)) # Expected 1
print(solution.searchInsert([1,3,5,6], 7)) # Expected 4