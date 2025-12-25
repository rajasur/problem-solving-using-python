#TODO - 680. Valid Palindrome II

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

"""
Time Complexity: O(n)
- In the worst case, we scan the entire string once with the outer while loop: O(n)
- If a mismatch is found, we call isPalindrome twice, each checking at most O(n) characters
- However, the total work done is still O(n) because we only make this check once
- Overall: O(n)

Space Complexity: O(1)
- We only use a constant amount of extra space for the left and right pointers
- The isPalindrome function uses only two pointer variables
- No additional data structures are created
- Overall: O(1)
"""

from typing import List

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left: str, right: str) -> bool:
            while (left < right):
                if s[left] != s[right]:
                    return False 
                left += 1 
                right -= 1 
            return True 
        
        left, right = 0, len(s) - 1
         
        while (left < right):
            if s[left] != s[right]: #First Mismatch
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            else:
                left += 1 
                right -= 1
        return True
                
            
        