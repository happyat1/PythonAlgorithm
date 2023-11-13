
from typing import List
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
class Solution:
      def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while True:           
            half = (left+right)//2
            if half * half == x : return half
            elif half * half > x:
                if  (half-1) * (half-1) <= x:
                    return half -1
                else:
                    right = half -1
            else:
                if  (half+1) * (half+1) > x:
                    return half
                elif (half+1) * (half+1) == x: 
                    return half+1
                else:
                    left = half +1     
    
  
#Input: x = 8
#Output: 2

s =Solution()

#x = 8 #Output: 2
#print (s.searchInsert(x))

x = 9 #Output: 3
print (s.mySqrt(9))