from typing import List 

# Optimal Solution TC[O(n)] and SC[O(1)]
def leftRotateByOnePlace(arr: List['int'], n: int) -> List['int']:
    temp = arr[0] 
    for i in range(1, n):
        arr[i-1] = arr[i] 
    arr[n-1] = temp 
    return arr 

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(f"Before Left Rotation {arr}")
    n = len(arr)
    res_left_rotation = leftRotateByOnePlace(arr, n)
    print(f"After Left Rotation by One Place {res_left_rotation}")
     