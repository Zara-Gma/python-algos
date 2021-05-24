# https://leetcode.com/problems/number-of-good-pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        Index        0 1 2
        Array Nums   1 1 1
            
            (0, 1) (0, 2) (1, 2)
            4*2 (each couple twice instead of once)
            +
            6 (each number with himself)
            =
            14
        '''
                       # i |
                       # j         |
        # Input: nums = [1,2,3,1,1,3]
        # Output: 2
        
        output = 0
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] == nums[j] and i < j:
                    output += 1
                    print(i, j)
        return output