'''
    Count number of vowels in a given string using recursion.
'''

VOWELS = ('a','e','i','o','u')

def count_vowels(str,n):
    if n<0:
        return 0
    if str[n] in VOWELS:
        return 1 + count_vowels(str, n-1)
    else:
        return count_vowels(str,n-1)
    
str = "Hello World!"
print(count_vowels(str,len(str)-1))

'''
Output:
3
'''