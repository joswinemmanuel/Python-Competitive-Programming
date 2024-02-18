from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*(product(l1, l2)))

'''
1 2
3 4
(1, 3) (1, 4) (2, 3) (2, 4)
'''
