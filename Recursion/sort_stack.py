'''
    Sort a given stack using recursion.
'''

def sort(stack):
    if len(stack)==1:
        return
    top = stack.pop()
    sort(stack)
    insert(stack,top)

def insert(stack, el):
    if not stack or stack[-1]:
        stack.append(el)
        return
    top = stack.pop()
    insert(stack,el)
    stack.append(top)

stack = [4,5,6,2,3,6,9,8]
stack.sort()
print(stack)

'''
Output:
[2, 3, 4, 5, 6, 6, 8, 9]
'''