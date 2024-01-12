from typing import List



class Solution:
    def maxProfit_bruteForcce(self, prices: List[int]) -> int:
        res = 0
        for i in range (len(prices)):
            profit = 0
            for j in range (i+1,len(prices)):
                profit = prices[j] -prices[i]
                res = max(profit, res)
                
        return res


    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0] # Store the possible lowest price to date
        for i in range (1,len(prices)):
            if prices[i] <= lowest: # Update the possible lowest price to date if lower found
               lowest = prices[i]
            elif (prices[i] -lowest > res):   
               res = prices[i] -lowest
        return res


s = Solution()
#Input: prices = [7,1,5,3,6,4]
#Output:Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
prices = [7,1,5,3,6,4]

print(s.maxProfit(prices))


#Input: prices = [7,6,4,3,1]
# Output: 0
prices = [7,6,4,3,1]

print(s.maxProfit(prices))