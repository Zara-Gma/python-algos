# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
#  That is, for each nums[i] you have to count the number of valid j's such that j != i 
# and nums[j] < nums[i].

# Return the answer in an array.

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        broadcasting
        smaller_nums: [0,0,0,0,0]
        #     Output: [4,0,1,1,3]
        """
        # Input: nums = [8,1,2,2,3]
        # Output: [4,0,1,1,3]
        # iterate through the array
        # compare the numbers and count how many are smaller than the previous one
        smaller_nums = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    smaller_nums[i]+= 1
        return smaller_nums
