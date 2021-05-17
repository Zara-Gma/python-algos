# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:
#                    |
# Input: address = "1.1.1.1"
# newaddress = "1[.]"
# Output: "1[.]1[.]1[.]1"

#Solution 1
class Solution(object):
    def defangIPaddr(self, address):
        # for i in range(len(address)):

        result = []
        for character in address:
            if character == '.':
                result += list("[.]")
            else:
                result.append(character)
            print(result)
        return "".join(result)

sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))


#Solution 2
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")
# https://leetcode.com/problems/richest-customer-wealth