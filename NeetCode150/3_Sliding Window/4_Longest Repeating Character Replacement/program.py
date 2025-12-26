#TODO - 424. Longest Repeating Character Replacement
"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

"""
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = [0] * 26
        left, right = 0, 0
        n = len(s)
        max_window = 0
        max_freq = 0
        
        while right < n:
            char_map[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, char_map[ord(s[right]) - ord('A')])
            
            windows_length = right - left + 1
            
            if windows_length - max_freq > k:
                char_map[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            windows_length = right - left + 1
            max_window = max(max_window, windows_length)
            right += 1
            
        return max_window

        
        
if __name__ == "__main__":
    s = "AABABBA" 
    k = 1
    sol = Solution()
    print(sol.characterReplacement(s, k))