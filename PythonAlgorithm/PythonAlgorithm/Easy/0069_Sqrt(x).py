
from typing import List
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
class Solution:
      def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:           
            middle = (left+right)//2
            if middle * middle == x : return middle
            elif middle * middle > x:
                if  (middle-1) * (middle-1) <= x:
                    return middle -1
                else:
                    right = middle -1
            else:
                if  (middle+1) * (middle+1) > x:
                    return middle
                elif (middle+1) * (middle+1) == x: 
                    return middle+1
                else:
                    left = middle +1     
    
  
#Input: x = 8
#Output: 2

s =Solution()

#x = 8 #Output: 2
#print (s.searchInsert(x))

x = 9 #Output: 3
print (s.mySqrt(9))