from itertools import groupby

n = input()
for k, g in groupby(n):
    print((len(list(g)), int(k)), end = ' ')

'''
1222311
(1, 1) (3, 2) (1, 3) (2, 1)
'''
