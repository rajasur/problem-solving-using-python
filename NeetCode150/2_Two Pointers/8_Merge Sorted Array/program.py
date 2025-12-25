#TODO - 88. Merge Sorted Array
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

"""
Merges two sorted arrays nums1 and nums2 into nums1 in-place.

This function merges nums2 into nums1 by comparing elements from the end of both arrays
and placing the larger element at the end of nums1. This approach avoids overwriting
elements in nums1 that haven't been processed yet.

Args:
    nums1 (List[int]): First sorted array with enough space at the end to hold elements 
                        from nums2. Length is m + n where the last n elements are zeros.
    m (int): Number of initialized elements in nums1.
    nums2 (List[int]): Second sorted array to be merged into nums1.
    n (int): Number of elements in nums2.

Returns:
    None: The function modifies nums1 in-place and doesn't return anything 
            (though the current implementation returns nums1).

Time Complexity: O(m + n)
    - We iterate through both arrays once, processing each element exactly once.
    - In the worst case, we process all m + n elements.

Space Complexity: O(1)
    - We only use a constant amount of extra space (the 'right' pointer).
    - The merge is done in-place without allocating additional data structures.
    - No recursion is used, so no additional stack space is required.

Example:
    >>> nums1 = [1, 2, 3, 0, 0, 0]
    >>> m = 3
    >>> nums2 = [2, 5, 6]
    >>> n = 3
    >>> Solution().merge(nums1, m, nums2, n)
    >>> print(nums1)
    [1, 2, 2, 3, 5, 6]

Algorithm:
    1. Start from the end of both arrays (positions m-1 and n-1).
    2. Compare elements and place the larger one at position 'right'.
    3. Move the corresponding pointer (m or n) and right pointer backwards.
    4. Continue until all elements from nums2 are processed.
    5. If nums2 is exhausted first, nums1 elements are already in correct position.
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = m + n - 1 

        while (n > 0):
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[right] = nums1[m - 1]
                m -= 1 
            else:
                nums1[right] = nums2[n - 1]
                n -= 1
            right -= 1
        return nums1
    
if __name__ == "__main__":
    nums1, m = [1,2,3,0,0,0], 3
    nums2, n = [2,5,6], 3 
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))
    