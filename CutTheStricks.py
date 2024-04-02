def cutTheSticks(arr):
    value = sorted(list(set(arr)))
    rs = [len(arr)]
    tmp = len(arr)
    for v in value:
        tmp -= arr.count(v)
        if tmp != 0:
            rs.append(tmp)
    return rs



n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print(result)
