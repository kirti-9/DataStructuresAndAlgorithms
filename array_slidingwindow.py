'''
    find max sum subarray, all distinct elements.
'''

def find_max(arr, k):
    left = 0
    right = 0
    MAX_SUM = -1
    window = set()
    current_sum = 0

    while True:
        if arr[right] not in window:
            window.add(arr[right])
            current_sum+=arr[right]
        else:
            window.remove(arr[left])
            left+=1
            right+=1
        if len(window)==k:
            if MAX_SUM < current_sum: MAX_SUM = current_sum
            window.remove(arr[left])
            current_sum-=arr[left]
            left+=1
        if right == len(arr)-1:
            return MAX_SUM
        
arr = [1, 2, 1, 3, 4]
k = 3

print(find_max(arr,k))
        
    