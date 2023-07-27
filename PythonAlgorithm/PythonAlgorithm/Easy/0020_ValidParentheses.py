
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')' , '[':']' , '{':'}'}
        res = []
        for c in s :
            if c in dic:
                res.append(c)
            else:
                if len(res)>0 and c == dic[res[-1]]:
                    del res[-1]
                else:
                    return False
        return res == []

#Input: strs = "{[()[]{}((([])))]}"
#Output: True

#Input: strs = "{[()[]{}((([])))]]}"
#Output: False

s =Solution()

strs = "{[()[]{}((([])))]}"
print (s.isValid(strs))
strs = "{[()[]{}((([])))]]}"
print (s.isValid(strs))

