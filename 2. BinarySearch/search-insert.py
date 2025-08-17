# Search Insert Position
'''
Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.

'''

from typing import List
def searchInsertPosition(arr: List[int], target: int) -> int:
    n = len(arr)
    ans = n 
    low, high = 0, (n-1)

    while(low <= high):
        mid = (low + high) // 2
        if (arr[mid] >= target):
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1 
    return ans 


if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6 
    index = searchInsertPosition(arr, x)
    print(f"Element has to be inserted at position {index}")
