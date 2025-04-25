'''
    Print numbers n to 1 recursively
'''

def fun(n):
    if n<=0:
        return
    print(n)
    fun(n-1)

n = 10
fun(n)

'''
Output:
10
9
8
7
6
5
4
3
2
1
'''