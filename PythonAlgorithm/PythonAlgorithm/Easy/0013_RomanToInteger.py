
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range (len(s)-1):
            value = dict[s[i]]
            if value >= dict[s[i+1]]:
                ans += value
            else :
                ans -=value
        ans += dict[s[-1]]
        print (ans)
        return ans       

dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        } 


#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
inputStr = "MCMXCIV"
s =Solution()
s.romanToInt(inputStr)