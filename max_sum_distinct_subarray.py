'''
    find max sum subarray, all distinct elements.
'''

def sum_arr(arr):
    sum = 0
    for a in arr:
        sum+=a
    return sum

def find_max(arr, k):
    left = 0
    right = k
    MAX_SUM = -1
    window = set()

    while right < len(arr):
        window = set(arr[left:right])
        if len(window)==k:
            MAX_SUM = max(MAX_SUM, sum_arr(window))
        left+=1
        right+=1

    return MAX_SUM
        
arr = [1, 2, 1, 3, 4]
k = 3

print(find_max(arr,k))
        
    