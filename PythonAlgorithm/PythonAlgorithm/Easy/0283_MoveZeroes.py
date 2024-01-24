
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range (len(nums)):
            if nums[i] != 0 :
                if i > index:
                    nums[index] = nums[i]
                    nums[i] = 0            
                index+= 1


#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

s =Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)

print(nums)

#Input: nums = [0]
#Output: [0]

nums = [0]
s.moveZeroes(nums)

print(nums)

#Input: nums = [0]
#Output: [0]

nums = [0,0,1,0,2,3,0,4,5,0,0,6,7,8,9,0,0]
s.moveZeroes(nums)

print(nums)