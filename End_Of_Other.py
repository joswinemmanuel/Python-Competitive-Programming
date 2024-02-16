def end_other(str1, str2):
   if len(str2) > len(str1):
      str1, str2 = str2, str1
   length = len(str2)
   return str1[-length:].lower() == str2.lower()

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(end_other('joswIN', 'win'))
print(end_other('and', 'agath'))
print(end_other('tH', 'agath'))
print(end_other('so', 'nose'))

'''
True
True
True
True
False
True
False
'''
