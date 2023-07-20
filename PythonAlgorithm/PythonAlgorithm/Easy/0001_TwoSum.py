from typing import List

class Solution:
    def twoSum_set(self, nums: List[int], target: int) -> List[int]:    
        numSet = set ()
        for i in range (len(nums)):
            needed = target - nums[i]
            if  needed not in numSet:
                numSet.add (nums[i])
            else:                
                return {i, nums.index(needed)}

    def twoSum_dict(self, nums: List[int], target: int) -> List[int]:    
        dict = {}
        for i in range (len(nums)):
            needed = target - nums[i]
            if  needed not in dict:
                dict[nums[i]]=i
            else:                
                return {i, dict[needed]}
            

nums = [2,7,11,15]
target = 9
s =Solution()
print(s.twoSum_set (nums,target))
print(s.twoSum_dict (nums,target))