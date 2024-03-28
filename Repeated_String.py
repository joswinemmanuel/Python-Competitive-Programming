def repeatedString(s, n):
    len_s = len(s)
    repeat_count = n // len_s
    remainder = n % len_s
    a_count = (s.count('a') * repeat_count) + s[:remainder].count('a')
    return a_count


s = input()
n = int(input())
print(repeatedString(s, n))


'''
aba
10
7
'''
