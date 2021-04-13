#1431. Kids With the Greatest Number of Candies
class Solution(object):
   def kidsWithCandies(self, candies, extraCandies):
    #Create an empty array to hold the candies
    listCandies = []
    # Iterate through the list of candies
    for candy in candies:
        #find the maximum number of candies
        maxNumber = max(candies)
        #get the totalNumberOfCandies by adding each candy and the extra candies
        totalNumberOfCandies = candy + extraCandies
        #If the totalNumberOfCandies is more than the input's maximum number the return true
        if totalNumberOfCandies >= maxNumber:
            #Add the candies to the empty array and return true ONLY if the condition is met
            listCandies.append(True)
        else:
            #Otherwise return false
            listCandies.append(False)
    return listCandies

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies