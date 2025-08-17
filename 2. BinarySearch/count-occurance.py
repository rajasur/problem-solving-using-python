'''
Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Examples

Example 1:
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.

Example 2:
Input: N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output: 5
Explanation: 2 is occurring 5 times in the given array so it is our answer.
'''

from typing import List 

class countOccurance:

    @staticmethod
    def first_occurance(arr: List[int], target: int) -> int:
        n = len(arr)
        low, high = 0, (n-1)
        ans = n 

        while(low <= high):
            mid = (low + high) // 2
            if (arr[mid] >= target):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1 

        return ans


    @staticmethod
    def last_occurance(arr: List[int], target: int) -> int:
        n = len(arr)
        low, high = 0, (n-1)
        ans = n 

        while(low <= high):
            mid = (low + high) // 2
            if (arr[mid] > target):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1 

        return ans
    
    @staticmethod
    def count_occurance(arr: List[int], target: int) -> int:
        first_occ = countOccurance.first_occurance(arr, target)
        last_occ = countOccurance.last_occurance(arr, target) - 1

        return (last_occ-first_occ+1)


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 2, 3]
    target = 2 
    result = countOccurance.count_occurance(arr, target)
    print(f"Number of occurance of the given number {target} is: {result}")
