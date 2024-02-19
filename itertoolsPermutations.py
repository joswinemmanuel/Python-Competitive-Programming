from itertools import permutations

s, n = input().split()
permutation = list(permutations(s, int(n)))

for i in sorted(permutation):
   print(''.join(i))

'''
HACK 2
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
