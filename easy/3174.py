"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the final_sing string after removing all digits.

Example 1:
    Input: s = "abc"
    Output: "abc"
    Explanation: There is no digit in the string.

Example 2:
    Input: s = "cb34"
    Output: ""
    Explanation: First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        final_s = []
        
        for char in s:
            if char.isdigit():
                if final_s:
                    final_s.pop()
            else:
                final_s.append(char)
            
        return "".join(final_s)

solution = Solution()

print(solution.clearDigits("abc"))  # Expected "abc"
print(solution.clearDigits("cb34")) # Expected ""