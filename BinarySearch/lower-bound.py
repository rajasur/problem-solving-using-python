# Lower Bound Implementation
'''
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x.

Example 2:
Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] >= x.
'''

# Time Complexity O(logbase2 n)

from typing import List

def lowerBound(arr: List[int], x: int) -> int:
    n = len(arr)
    ans = n
    low = 0
    high = n-1 
    
    while(low <= high):
        mid = (low + high) // 2
        if (arr[mid] >= x):
            ans = mid 
            high = mid-1 
        else:
            low = mid+1 
    return ans

if __name__ == "__main__":
    arr = [3, 5, 8, 1, 5, 19]
    x = 9
    ind = lowerBound(arr, x)
    print(f"The lower bound index is {ind}") 