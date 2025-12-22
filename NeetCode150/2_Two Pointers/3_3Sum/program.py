#TODO - 15. 3Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List

"""
Time Complexity: O(n²)
- Sorting: O(n log n)
- Outer loop: O(n)
- Inner two pointers: O(n)
- Overall: O(n log n) + O(n²) = O(n²)

Space Complexity: O(1) or O(n)
- O(1) if we don't count the output array
- O(n) if we count the space for sorting (depending on sort implementation)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue 
            j = i + 1 
            k = n - 1 
            
            while (j < k):
                target = nums[i] + nums[j] + nums[k]
                
                if target < 0:
                    j += 1
                elif target > 0:
                    k -= 1 
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1 
        return result 
    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(nums))
     
                 
                