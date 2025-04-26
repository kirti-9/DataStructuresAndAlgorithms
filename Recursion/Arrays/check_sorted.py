'''
    Check if given array is sorted using recursion.
'''

def is_sorted(arr,n):
    if n <=0:
        return True
    if arr[n]>arr[n-1]:
        return is_sorted(arr,n-1)
    else:
        return False
    
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,3]

print(f'Is {arr1} in sorted order? {is_sorted(arr1, len(arr1)-1)}')
print(f'Is {arr2} in sorted order? {is_sorted(arr2, len(arr2)-1)}')