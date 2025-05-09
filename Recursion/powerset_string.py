'''
Given a string, return all possible subsets (the power set).
The power set is the set of all subsets of a set, including the empty set and the set itself.
or 
print all subsets. 
or
print all subsequences.
For example, given the string "abc", the power set is:
[
    "",
    "a",
    "b",
    "c",
    "ab",
    "ac",
    "bc",
    "abc"
]
'''

def powerset(ip, op):
    if len(ip) == 0:
        power_set.append(op)
        return
    op1 = op
    op2 = op + ip[0]
    ip_list = list(ip)
    del ip_list[0]
    ip = ''.join(ip_list)
    powerset(ip, op1)
    powerset(ip, op2)

ip = 'abc'
op = ''
power_set = []
powerset(ip, op)
print(power_set)

'''
Output:
['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
'''

ip = 'abcb'
op = ''
power_set = []
powerset(ip, op)
print(power_set)

'''
Output:
['', 'b', 'c', 'cb', 'b', 'bb', 'bc', 'bcb', 'a', 'ab', 'ac', 'acb', 'ab', 'abb', 'abc', 'abcb']
'''