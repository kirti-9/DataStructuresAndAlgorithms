'''
    Print nth item in fibonacci sequence.
'''

def fibonacci(n):
    if n <=1:
        return n
    if n < 0:
        raise ValueError("wrong input ")
    return fibonacci(n-1)+fibonacci(n-2)


n = 10
print(f'The fibonacci series upto {n} items is: {fibonacci(n-1)}')

'''
Output
The fibonacci series upto 10 items is: 34
'''