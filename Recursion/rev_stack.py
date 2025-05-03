'''
    Reverse a given stack using recursion.
'''

def rev(stack):
    if not stack:
        return
    top = stack.pop()
    rev(stack)
    push(stack,top)

def push(stack,element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    push(stack,element)
    stack.append(top)

stack = [1,2,3,4,5,6]
rev(stack)
print(stack)

'''
Output:
[6, 5, 4, 3, 2, 1]
'''