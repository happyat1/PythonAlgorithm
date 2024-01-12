
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Create an array list to store the output result...
        res = []*numRows
        # Add the first row
        res.append([1])
        # Add other rows
        for i in range (1,numRows):
            curr  = []
            # Add the first number
            curr .append(1)
            # Calculate for each of the next values...
            for j in range (0,i-1):
                curr .append(prev[j]+prev[j+1])
            
            # Add the last number
            curr .append(1)

            # Store the value in the Output array...
            res.append(curr)
             
            # Set prev is equal to curr.
            prev = curr 

        return res


s = Solution()
#Input: 5
#Output:last list [1, 4, 6, 4, 1]
print(s.generate(10))

#Input: 10
#Output:last list [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
print(s.generate(10))