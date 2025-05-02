'''
    Sort a given array using recursion.
'''

def sort(arr):
    if len(arr)==1:
        return
    el = arr.pop()
    sort(arr)
    insert(arr,el)   # Insert the popped element back into the sorted array at the right position

def insert(arr,el):
    if len(arr)==0 or arr[-1]<=el:
        arr.append(el)
        return
    last_el = arr.pop()
    insert(arr,el)
    arr.append(last_el)
    return

arr = [2,3,7,6,4,5,4]
sort(arr)
print(arr)

'''
Output:
[2, 3, 4, 4, 5, 6, 7]
'''
