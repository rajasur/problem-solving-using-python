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
            
                
            
        