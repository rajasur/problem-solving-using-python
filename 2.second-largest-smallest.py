#Bruteforce Solution (TC: O(nlogn) + O(n))
def bruteForceSecondLargest(arr, n):
    if  (n < 2):
        return -1
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for k in range(n-2, 1 , -1):
        if (arr[k-1] != arr[k]):
            return arr[k-1]
        
def bruteForceSecondSmallest(arr, n):
    second_smallest = float('inf')
    if (n < 2):
        return -1 
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
    for k in range(n-2, -1, -1):
        if (arr[k] != arr[k+1]):
            second_smallest = arr[k]
            return second_smallest
        
        
#Better Solution (TC: O(2n))
def betterSolutionSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            small = arr[i]
    second_samll = float('inf')
    for k in range(n):
        if (arr[k] > small and arr[k] < second_samll):
            second_samll = arr[k]
    return second_samll

def betterSolutionLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            large = arr[i] 
    for k in range(n):
        if (arr[k] < large and arr[k] > second_large):
            second_large = arr[k]
    return second_large

# Optimal Solution (TC: O(n)) 
def secondLagrgest(arr,n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large=large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large

#Optimal Solution (TC: O(n))
def secondSmallest(arr,n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small 
            small = arr[i]
        elif (arr[i]<second_small and arr[i] != small):
            second_small = arr[i] 
    return second_small

if __name__ == '__main__':
    arr=[1,2,4,7,7,5]
    n=len(arr)
    res_bruteforce_solution_large = bruteForceSecondLargest(arr, len(arr))
    res_bruteforce_solution_small = bruteForceSecondSmallest(arr, n)
    res_optimal_solution_large = secondLagrgest(arr, n)
    res_optimal_solution_small = secondSmallest(arr, n)
    res_beeter_solution_smallest = betterSolutionSmallest(arr, n)
    res_beeter_solution_largest = betterSolutionLargest(arr, n)
    print(f"Bruteforce solution of second largest {res_bruteforce_solution_large}")
    print(f"Bruteforce solution of second smallest {res_bruteforce_solution_small}")
    print(f"Better soulution of second largest result is {res_beeter_solution_largest}")
    print(f"Better soulution of second smallest result is {res_beeter_solution_smallest}")
    print(f"Optimal solution of second Largest element is {res_optimal_solution_large}")
    print(f"Optimal solution of second Smallest elemnt is {res_optimal_solution_small}")
    
     