'''
    Tower of Hanoi
'''

def tower(n, s, d, h):
    if n == 1:
        print(f'Move Plate {n} from {s} to {d}')
        return
    tower(n-1, s, h, d)
    print(f'Move plate {n} from {s} to {d}')
    tower(n-1, h, d, s)

n = 3 
s = 'rod A'
d = 'rod C'
h = 'rod B'
tower(n,s,d,h)

'''
Output:
Move Plate 1 from rod A to rod C
Move plate 2 from rod A to rod B
Move Plate 1 from rod C to rod B
Move plate 3 from rod A to rod C
Move Plate 1 from rod B to rod A
Move plate 2 from rod B to rod C
Move Plate 1 from rod A to rod C
'''
