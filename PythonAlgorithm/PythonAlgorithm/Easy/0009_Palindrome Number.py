from typing import List

# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        string = str(x)
        length  = len(string)
        l = 0
        r = length -1
        while l < r:
            if string[l] != string [r]: return False
            l += 1
            r -= 1
        
        return True

            
    def isPalindrome_oneLine(self, x: int) -> bool:
        return str(x) == str(x)[::-1] # nothing fancy , just syntactic sugar

#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.


#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


s =Solution()
x = 121
print(s.isPalindrome (x)) #Output: true


x = -121
print(s.isPalindrome (x)) #Output: false
