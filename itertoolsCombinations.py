from itertools import combinations

a, b = input().split()
a = sorted(a)

for i in range(int(b)):
    for j in combinations(a, i+1):
        print(''.join(j))

'''
HACK 2
A
C
H
K
AC
AH
AK
CH
CK
HK
'''
