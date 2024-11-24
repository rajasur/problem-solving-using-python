def checkingArraySorting(arr, n):
    if (n < 1):
        return -1 
    for i in range(n-1):
        if (arr[i+1] >= arr[i]):
            pass 
        else:
            return "Array is not sorted."
    return "Array is sorted."
        
if __name__ == "__main__":
    arr = [1,2,4,7,7,5]
    sorted_array = sorted(arr)
    n = len(arr)
    sorted_checking = checkingArraySorting(sorted_array, n)
    print(sorted_checking)