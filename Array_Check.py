def arrayCheck(lst):
   for i in range(len(lst)-2):
      if lst[i]==1 and lst[i+1]==2 and lst[i+2]==3:
         return True
   return False


print(arrayCheck([1, 2, 3, 4]))
print(arrayCheck([1, 1, 2, 3, 4]))
print(arrayCheck([1, 1, 4, 5]))

'''
True
True
False
'''
