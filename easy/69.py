"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
 
Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

class Solution:
    def mySqrt(x: int) -> int:
        if (x == 0 or x == 1):
            return x
        
        start, end = 2, x

        while (start <= end):
            mid = start + (end - start) // 2

            if (mid * mid == x):
                return mid
            elif (mid * mid < x):
                start = mid + 1
            else:
                end = mid - 1
        return end

solution = Solution()

print(solution.mySqrt(0))   # Expected 0
print(solution.mySqrt(1))   # Expected 1
print(solution.mySqrt(4))   # Expected 2
print(solution.mySqrt(8))   # Expected 2
print(solution.mySqrt(9))   # Expected 3
print(solution.mySqrt(16))  # Expected 4
print(solution.mySqrt(25))  # Expected 5
print(solution.mySqrt(36))  # Expected 6
print(solution.mySqrt(49))  # Expected 7
print(solution.mySqrt(64))  # Expected 8
print(solution.mySqrt(81))  # Expected 9
print(solution.mySqrt(100)) # Expected 10