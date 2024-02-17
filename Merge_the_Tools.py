def merge_the_tools(string, k):
   for i in range(0, len(n), k):
      res = ''
      for j in string[i:i+k]:
         if j not in res:
            res += j
      print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

'''
AABCAAADA
3
AB
CA
AD
'''
