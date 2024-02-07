from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range (1,len(nums)):
            res = res^nums[i]

        return res


    #Note: this approach won’t work for negative numbers. But it can be tweaked to work for both negative and positive numbers
    def singleNumber_General(self, nums: List[int]) -> int: #  every element occurs 3 times, except one element which occurs only once. 
        res = 0
        INT_SIZE = 32
        n = len(nums)

        # Iterate through every bit
        for i in range(0, INT_SIZE) :
         
            # Find sum of set bits 
            # at ith position in all 
            # array elements
            sm = 0
            x = (1 << i)
            for j in range(0, n) :
                if (nums[j] & x) :
                    sm = sm + 1
                 
            # The bits with sum not multiple of 3 (or any other number), are the
            # bits of element with single occurrence.
            if ((sm % 3)!= 0) :
                res = res + x
     
        return res

    #Note: this updated approach work for both negative and positive numbers
    def singleNumber_GeneralPlus(self, nums: List[int]) -> int: #  every element occurs 3 times, except one element which occurs only once. 
        res = 0
        INT_SIZE = 32
        negative_count = 0
        n = len(nums)

        # Convert negative numbers into abs(numbers) and record negative_count
        for j in range(n) :
            num_c = nums[j]
            if num_c < 0:
                negative_count += 1
                num_c = abs(nums[j])
                nums[j]=num_c

        # Iterate through every bit
        for i in range(0, INT_SIZE) :
         
            # Find sum of set bits 
            # at ith position in all 
            # array elements
            sm = 0
            x = (1 << i)
            for j in range(0, n) :
                if (nums[j] & x) :
                    sm = sm + 1
                 
            # The bits with sum not multiple of 3 (or any other number), are the
            # bits of element with single occurrence.
            if ((sm % 3)!= 0) :
                res = res + x

        if negative_count%2 ==1:
           res = res * (-1) 
        return res



s = Solution()
#Input: Input: nums = [2,2,1]
#Output: 1
#nums = [2,2,1]
#print(s.singleNumber(nums))

#Input: Input: nums = [4,1,2,1,2]
#Output: 4
#nums = [4,1,2,1,2]
#print(s.singleNumber(nums))

#nums = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
#print("The element with single occurrence is ", s.singleNumber_General(nums))

nums =  [12, 1, 12, -3, 12, 1, 1, -2, -3, -2, -2,-3, -7]
print("The element with single occurrence is ", s.singleNumber_GeneralPlus(nums))