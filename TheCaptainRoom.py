n = int(input())
f = list(map(int, input().split()))
x = {}

for i in f:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

for i in x:
    if x[i] == 1:
        print(i)
        break

'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
8
'''
