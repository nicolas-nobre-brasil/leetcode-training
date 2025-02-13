"""
Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap 
is an operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing 
at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with one string swap.

Example 3:
    Input: s1 = "kelb", s2 = "kelb"
    Output: true
    Explanation: The two strings are already equal, so no string swap operation is required.
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
            if s1 == s2: return True
        
            count_diff = 0
            diffs = []
        
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count_diff += 1
                    diffs.append((s1[i], s2[i]))
        
        
            return count_diff == 2 and diffs[0] == diffs[1][::-1]

solution = Solution()

solution.areAlmostEqual("bank", "kanb")     # Expected True
solution.areAlmostEqual("attack", "defend") # Expected False
solution.areAlmostEqual("kelb", "kelb")     # Expected True