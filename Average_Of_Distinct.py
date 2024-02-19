def average(array):
    n = set(array)
    return sum(n)/len(n)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

'''
10
161 182 161 154 176 167 171 170 174
169.375
'''
