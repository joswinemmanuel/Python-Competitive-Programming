def count_evens(l):
   return len(list((filter(lambda n: n%2 == 0, l))))

print(count_evens([1, 2, 2, 3, 4]))
print(count_evens([1, 1, 2, 3, 4]))
print(count_evens([1, 2, 2, 10, 4]))
print(count_evens([2, 2, 2, 3, 4]))

'''
3
2
4
4
'''
