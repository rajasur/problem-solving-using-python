# TODO - 238. Product of Array Except Self
"""
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List

#NOTE - TC O(n) & SC O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left = [1] * n
#         right = [1] * n
#         ans = [1] * n
        
#         # Build left product array
#         left[0] = 1
#         for i in range(1, n):
#             left[i] = left[i - 1] * nums[i - 1]
        
#         # Build right product array
#         right[n - 1] = 1
#         for j in range(n - 2, -1, -1):
#             right[j] = right[j + 1] * nums[j + 1]
        
#         # Build answer
#         for k in range(n):
#             ans[k] = left[k] * right[k]
        
#         return ans

#NOTE - TC O(n) & SC O(1)
class Solutions:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n 
        
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1] 
        
        temp = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * temp 
            temp = temp * nums[i]
        return ans
            


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solutions()
    print(sol.productExceptSelf(nums))

