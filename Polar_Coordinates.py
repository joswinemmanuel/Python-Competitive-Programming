import cmath
c = complex(input())
print((c.real**2 + c.imag**2) ** (1/2))
print(cmath.phase(c))

'''
1+2j
2.23606797749979
1.1071487177940904
'''
