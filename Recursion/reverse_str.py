'''
    Reverse a string using recursion.
'''

def rev(str,n):
    if n <0:
        return 
    print(str[n],end='')
    rev(str,n-1)

str = "Hello World!"
print(f'Reverse of string {str} is: ', end="")
rev(str,len(str)-1)

'''
Output:
Reverse of string Hello World! is:!dlroW olleH
'''
