from calendar import weekday, day_name

date = list(map(int, input().split()))
print(day_name[weekday(date[2], date[0], date[1])].upper())


'''
08 05 2015
WEDNESDAY
'''
