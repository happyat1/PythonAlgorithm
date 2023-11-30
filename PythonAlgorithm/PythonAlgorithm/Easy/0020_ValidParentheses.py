
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')' , '[':']' , '{':'}'}
        stack = []
        for c in s :
            if c in dict:
                stack.append(c)
            else:
                if len(stack)>0 and c == dict[stack[-1]]:
                    del stack[-1]
                else:
                    return False
        return stack == []

#Input: strs = "{[()[]{}((([])))]}"
#Output: True

#Input: strs = "{[()[]{}((([])))]]}"
#Output: False

s =Solution()

strs = "{[()[]{}((([])))]}"
print (s.isValid(strs))
strs = "{[()[]{}((([])))]]}"
print (s.isValid(strs))

