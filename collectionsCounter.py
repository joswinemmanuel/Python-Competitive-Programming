from collections import Counter

n = int(input())
available = list(map(int, input().split()))
count = Counter(available)

sum = 0
for i in range(int(input())):
   s, p = map(int, input().split())
   if s in count:
      if count[s] > 0:
         sum += p
   count[s] -= 1

print(sum)

'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
200
'''
