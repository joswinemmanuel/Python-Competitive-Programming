def fun(s):
    if ('@' not in s) or ('.' not in s) or (' ' in s):
        return False
    if s.count('@') > 1:
        return False
    if s.count('.') > 1:
        return False
    s = s.replace('@', ' ')
    s = s.replace('.', ' ')
    l = s.split()
    if len(l) < 3:
        return False
    for j in l[0]:
        if j.isalnum() == False and j != '_' and j != '-':
            return False
    for j in l[1]:
        if j.isalnum() == False:
            return False
    if len(l[2]) > 3 or len(l[2]) == 0:
        return False
    return True
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


'''
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
