'''
    Print fibonacci series upto n numbers.
'''

def fib(n):
    if n <=1:
        return n
    if n <0:
        raise ValueError("Wrong input")
    return fib(n-1)+fib(n-2)

n = 10
for i in range(0, n):
    print(fib(i), end=", ")

'''
Output:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 
'''
    