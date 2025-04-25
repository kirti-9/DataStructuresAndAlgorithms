'''
    Factorial of a number using recursion
'''

def factorial(n):
    if n < 1:
        return 1
    return n*factorial(n-1)

n = 5
print("Factorial of", n, "is:", factorial(n))

'''
Output
Factorial of 5 is: 120
'''
    