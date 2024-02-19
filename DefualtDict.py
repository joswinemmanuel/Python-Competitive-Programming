n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(str(input()))
for i in range(m):
    b.append(str(input()))
for i in b:
    if i not in a:
        print(-1)
    else:
        for j in range(n):
            if i==a[j]:
                print(j+1, end = ' ')
        print()

'''
Sample Input
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output
1 2 4
3 5
'''
