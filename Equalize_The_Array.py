def equalizeArray(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return len(arr)-max(d.values())


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(equalizeArray(arr))

'''
5
3 3 2 1 3
2
'''
