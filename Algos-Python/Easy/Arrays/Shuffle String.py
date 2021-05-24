# https://leetcode.com/problems/shuffle-string/
# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

        # Input: s = "codeleet", indices = [4,5,6,7,0,1,2,3]     
        # Output: "leetcode"
        
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ['.'] * len(s)
        for i in range(len(s)):
            output[indices[i]] = s[i]
        return "".join(output)
