
from typing import List

 #You may assume that the majority element always exists in the array.
class Solution:
    #Time Complexity: O(nlogn), Sorting requires O(n log n) time complexity.
    #Auxiliary Space: O(1), As no extra space is required.
    def majorityElement_sorting(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        if length ==1:
            return nums[0]
        count = 1
        pre = nums[0]      
        for i in range(1, length):
            if nums[i] == pre:
                count+=1
                if count >= (0.5 * length):
                    return nums[i]
            else :
                pre = nums[i]
                count = 1


    #Time Complexity: O(n), O(n) ( For one pass over the array ).
    # Note: If it cannot be assumed that the majority element always exists in the array.
    # We need to check using the 2nd traversal to see whether its count is greater than N/2.
    #Auxiliary Space: O(1), As no extra space is required.

    #Why does the algorithm work?
    #Consider all the possible cases:
    #    1. The first number is the right cadidate
    #        a. count never becomes 0 --> good
    #        b. count becomes 0 --> repeat with the rest of the numbers

    #    2. The first number is not the right cadidate
    #        a. count becomes 0 for sure --> repeat with the rest of the numbers
    #         

    def majorityElement_mooreVoting(self, nums: List[int]) -> int:
        # Step 1: Find a candidate for the majority element
        candidate = None
        count = 0
    
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
    
        # Step 2: Verify if the candidate is the majority element ( No need for step 2 if you may assume that the majority element always exists in the array.)
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
    
        if count > len(nums) // 2:
            return candidate
        else:
            return None  # No majority element found



#Input: nums = [2,2,1,1,1,2,2]
#Output: 2

s =Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement_sorting(nums))
print(s.majorityElement_mooreVoting(nums))

#Input: nums = [2,2,2,1,1,1,3,4,3,3,3,2]
#Output: None

nums = [2,2,2,1,1,1,3,4,3,3,3,2]
print(s.majorityElement_sorting(nums))
print(s.majorityElement_mooreVoting(nums))