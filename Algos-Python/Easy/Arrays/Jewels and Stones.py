class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int: 
#   https://leetcode.com/problems/jewels-and-stones/submissions/              
  #         Input: jewels = "aA", stones = "aAAbbbb"
  #         Output: 3      
       
        output = 0
        for i in range (len(jewels)):
            for j in range (len(stones)):
                if jewels[i] == stones[j]:
                    output += 1
        return output