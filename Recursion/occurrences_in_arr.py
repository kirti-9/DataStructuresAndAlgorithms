'''
    Count occurences of an element
'''

def occur(arr,el,n):
    if n <0:
        return 0
    elif arr[n]==el:
        return 1 + occur(arr,el,n-1)
    else:
        return 0+occur(arr,el,n-1)
    
arr = [1,2,3,1,1,4,5,1,6,1]
el = 1
print(f'The element {el} occurs {occur(arr,el,len(arr)-1)} times in the {arr}')

'''
Output:
The element 1 occurs 5 times in the [1, 2, 3, 1, 1, 4, 5, 1, 6, 1]
'''