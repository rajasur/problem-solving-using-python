#TODO - 1768. Merge Strings Alternately
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

"""
Time Complexity: O(n + m) where n = len(word1) and m = len(word2)
- The while loop runs min(n, m) times
- Appending remaining characters takes O(max(n, m) - min(n, m))
- join() operation is O(n + m)
- Overall: O(n + m)

Space Complexity: O(n + m)
- result list stores all characters from both strings
- Final merged string also takes O(n + m) space
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 
        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i += 1 
            j += 1 

        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)
    
if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    sol = Solution()
    print(sol.mergeAlternately(word1, word2))
    