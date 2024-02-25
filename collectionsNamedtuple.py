from collections import namedtuple
n = int(input())
Student = namedtuple("Student", input())
print(sum([int(Student(*input().split()).MARKS) for i in range(n)]) / n)

'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
78.00
'''
