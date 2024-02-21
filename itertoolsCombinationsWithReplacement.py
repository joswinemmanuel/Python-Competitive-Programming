from itertools import combinations_with_replacement

a, b = input().split()
a = sorted(a)

for i in combinations_with_replacement(a, int(b)):
    print(''.join(i))

'''
HACK 2
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
