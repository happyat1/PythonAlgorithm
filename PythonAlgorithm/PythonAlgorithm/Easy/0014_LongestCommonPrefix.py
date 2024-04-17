
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs:                
                if len(string)< i+1 or string[i] != char:
                   return ans
            ans += char
        return ans


#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

s =Solution()

strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(s.longestCommonPrefix(strs))