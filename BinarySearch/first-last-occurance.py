"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

Example 3:
Input: nums = [], target = 0
Output: [-1, -1]
"""

from typing import List

class Solution:
    @staticmethod
    def first_occurrence(arr: List[int], target: int) -> int:
        """Finds the first index where target appears."""
        n = len(arr)
        low, high = 0, n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    @staticmethod
    def last_occurrence(arr: List[int], target: int) -> int:
        """Finds the first index where an element greater than target appears."""
        n = len(arr)
        low, high = 0, n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    @staticmethod
    def search_range(nums: List[int], target: int) -> List[int]:
        """Returns the start and end index of the target in nums."""
        first = Solution.first_occurrence(nums, target)
        last = Solution.last_occurrence(nums, target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, last - 1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = Solution.search_range(nums, target)
    print(res)