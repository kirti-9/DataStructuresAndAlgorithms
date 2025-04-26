'''
    Find sum of all elements of an array recursively.
'''

def sum(arr, n):
    if n < 0:
        return 0
    return arr[n] + sum(arr, n-1)

arr = [1,2,3,4,5]
print(f'The sum of all elements of {arr} is: {sum(arr, len(arr)-1)}')

'''
Output:
The sum of all elements of [1, 2, 3, 4, 5] is: 15
'''