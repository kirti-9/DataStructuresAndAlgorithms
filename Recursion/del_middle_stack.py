'''
    Delete the middle element in a given stack. 

    Note: 
    for even length, there are two central elements, by convention, we delete the lower of the two.
'''

def del_middle(stack,n):
    if n//2 == len(stack)-1:
        stack.pop()
        return
    top = stack.pop()
    del_middle(stack,n)
    stack.append(top)

stack_odd = [0,1,5,2,7,9,3]
stack_even = [0,1,5,3,4,8]

del_middle(stack_odd, len(stack_odd))
del_middle(stack_even, len(stack_even))

print(stack_odd)
print(stack_even)

'''
Output:
[0, 1, 5, 7, 9, 3]
[0, 1, 5, 4, 8]
'''