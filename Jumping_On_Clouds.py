def jumpingOnClouds(n, c, k):
    energy = 100
    jump = 0
    while True:
        jump = (jump + k) % n
        energy -= 1
        if c[jump]:
            energy -= 2
        if jump == 0:
            break
    return energy

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(n, c, k)
print(result)


'''
8 2
0 0 1 0 0 1 1 0
92

4 2
0 0 1 0
96
'''
