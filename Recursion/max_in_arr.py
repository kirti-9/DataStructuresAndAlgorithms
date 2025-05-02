'''
    Find max element of the array using recursion
'''
import sys

def maximum(arr, n, max):
    if n <0 :
        return max
    if arr[n] > max:
        max = arr[n]
    return maximum(arr, n-1, max)

max = -1*(sys.maxsize)
arr = [2,4,5,1,9,5]
print(f'The maximum number in {arr} is: {maximum(arr,len(arr)-1, max)}')

'''
Output:
The maximum number in [2, 4, 5, 1, 9, 5] is: 9
'''
