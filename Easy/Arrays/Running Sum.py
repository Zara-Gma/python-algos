#1480. Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:  
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
# Example 1:  
    Index:       0 1 2 3 4
# Input: nums = [1,2,3,4]
"""

#Solution
class Solution(object):
    def runningSum(self, nums):
        for i in range(len(nums)-1):
            print('my index', i)
            nums[i+1] += nums[i]
        return nums
# https://leetcode.com/problems/running-sum-of-1d-array

sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
