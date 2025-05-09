'''
    Print all the unique subsets of a given string.
'''

def unique_set(ip, op):
    if len(ip) == 0:
        powerset.add(op)
        return
    op1 = op
    op2 = op + ip[0]
    list_ip = list(ip)
    del(list_ip[0])
    ip = ''.join(list_ip)
    unique_set(ip,op1)
    unique_set(ip, op2)

ip = 'abb'
op = ''
powerset = set()
unique_set(ip,op)
print(powerset)

'''
Output:
{'', 'ab', 'b', 'abb', 'a', 'bb'}
'''

