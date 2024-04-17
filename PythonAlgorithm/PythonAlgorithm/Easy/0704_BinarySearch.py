
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) -1  
        middle = 0
        while low <= high:
            middle = (low + high)//2
            if nums[middle] == target: return middle
            if nums[middle] < target: low = middle +1
            if nums[middle] > target: high = middle -1       

        return -1


#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4



s =Solution()

nums = [-1,0,3,5,9,12]
target = 9 #Output: 4
print (s.search(nums,target))

#Input: nums = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in nums so return -1

nums = [-1,0,3,5,9,12]
target = 2 #Output: -1
print (s.search(nums,target))