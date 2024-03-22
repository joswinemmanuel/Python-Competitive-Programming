def lof(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    l = [(b, a) for a,b in d.items()]

    for i, j in sorted(l, reverse=True):
        print(j, end=' ')


lof('banana')

'''
a n b
'''
