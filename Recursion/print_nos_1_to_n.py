'''
    Print numbers from 1 to n using recursion.
'''

def fun(n):
    if n<1:
        return
    fun(n-1)
    print(n)
    

n = 10
fun(n)

'''
Output:
1
2
3
4
5
6
7
8
9
10
'''