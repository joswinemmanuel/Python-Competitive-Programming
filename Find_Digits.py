def findDigits(n):
    count = 0
    for i in str(n):
        try:
            if n % int(i) == 0:
                count += 1
        except:
            pass
    return count

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    result = findDigits(n)
    print(result)

'''
2
12
1012
2
3
'''
