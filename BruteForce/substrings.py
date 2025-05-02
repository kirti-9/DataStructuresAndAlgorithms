'''
    Find all substrings from the given string.
'''

def substrings(str):
    subs=[]
    for i in range(len(str)):
        for j in range(i,len(str)):
            subs.append(str[i:j+1])
    return subs

str = 'abc'
print(substrings(str))