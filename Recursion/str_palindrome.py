'''
    Check if a given string is palindrome using recursion.
'''

def is_palindrome(str,n,i):
    if n == i or n == i-1:
        return True
    elif str[n]==str[i]:
        return is_palindrome(str,n-1,i+1)
    else:
        return False

str1 = "Hello"
str2 = "nitin"
print(is_palindrome(str1,len(str1)-1,0))
print(is_palindrome(str2,len(str2)-1,0))

'''
Output:
False
True
'''