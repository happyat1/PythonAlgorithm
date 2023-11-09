
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        prev_2 = 1 #n=1
        prev_1 = 2 #n=2
        
        if n<3: return n
        for i in range (3,n) :
            prev_1, prev_2 =prev_1 + prev_2, prev_1

        return prev_1 + prev_2

  
#Input: n=3
#Output: 3

s =Solution()
n =1 #Output: 1
print (s.climbStairs(n))
n =3 #Output: 3
print (s.climbStairs(n))
n =4 #Output: 5
print (s.climbStairs(n))
n =10 #Output: 89
print (s.climbStairs(n))
n =15 #Output: 987
print (s.climbStairs(n))