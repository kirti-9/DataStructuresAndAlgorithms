'''
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example:
n = 4, k = 5
Row 1: 0

Row 2: 01

Row 3: 0110

Row 4: 01101001
→ 5th symbol = 1

Explanation: The 4th row is "01101001", so the 5th character (1-indexed) is '1'.
'''

def kthGrammar(n,k):
    if k > 2**n-1:
        return -1
    if n==0 and k == 0:
        return 0
    # calculate mid index of nth row. length of nth row = 2^n
    mid = ((2**n)-1)//2
    # Post pattern observation, row_n[0:mid] == row_n-1
    if k <= mid:
        return kthGrammar(n-1,k)
    elif k > mid:
        # row_n[mid:] == !(row_n-1) and new_k --> if k = 5, mid = 3, new_k = 1
        # invert the digits, 1 to 0, and 0 to 1. bitwise not (~) will not work becuase it gives 2's complement.
        # write down the values of n rows and observe the pattern for better understanding.
        return 1-(kthGrammar(n-1,k-(mid+1))) 
    
    
n = 4
k = 2
print(kthGrammar(n-1,k-1))

n = 4
k = 6
print(kthGrammar(n-1,k-1))

n = 5
k = 13
print(kthGrammar(n-1,k-1))

'''
Output:
1
0
0

Explanation:
n = 4, i.e., 4th row:
0 1 1 0 1 0 0 1

n = 5 
0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
'''
