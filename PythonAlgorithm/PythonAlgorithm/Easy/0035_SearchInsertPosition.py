
from typing import List

class Solution:
      def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            middle = (left + right)//2
            if nums[middle] == target :
                return middle
            elif  nums[middle] > target :  
                right = middle -1
            elif nums[middle] < target :      
                left = middle +1

        if nums[left] >= target : 
            return left
        else:
            return left+1
    
  
#Input: nums = [1,3,5,6], target = 2
#Output: 1

s =Solution()

nums = [1,3,5,6]
target = 5 #Output: 2
print (s.searchInsert(nums,target))
target = 2 #Output: 1
print (s.searchInsert(nums,target))
target = 7 #Output: 4
print (s.searchInsert(nums,target))
target = 0 #Output: 0