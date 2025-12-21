#TODO - 271. Encode and Decode Strings 
"""
Description
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List 

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            right = left

            # Move right pointer until we find the '#' delimiter
            while s[right] != '#':
                right += 1

            # Extract the length of the next string (substring before '#')
            length = int(s[left:right])

            # Extract the actual string using the length and append to result
            # Start after '#' (right+1) and read 'length' characters
            res.append(s[right+1:right+1+length])

            # Move left pointer to the start of next encoded string
            left = right + 1 + length

        return res
    

# Example usage (for local testing)
if __name__ == "__main__":
    codec = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "", "#hash"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)

    print("Encoded:", encoded)
    print("Decoded:", decoded)