#TODO - Contains Duplicate
"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

#NOTE - TC O(n) and SC O(n)

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set() #NOTE - Taking Hash Set here
        for number in nums:
            if number in number_set:
                return True 
            number_set.add(number)
        return False 
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    result = Solution()
    print(result.hasDuplicate(arr))