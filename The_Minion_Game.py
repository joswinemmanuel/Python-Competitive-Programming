def minion_game(string):
   n = len(string)
   vowel = 'AEIOU'
   kevin = 0
   stuart = 0
   for i in range(n):
      if string[i] in vowel:
         kevin += n - i
      else:
         stuart += n - i
   if kevin > stuart:
      print(f'Kevin {kevin}')
   elif stuart > kevin:
      print(f'Stuart {stuart}')
   else:
      print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
BANANA
Stuart 12
'''
