for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a/b))
    except ZeroDivisionError:
        print("Error Code:", "integer division or modulo by zero")
    except Exception as e:
        print("Error Code:", e)


'''
3
1 0
2 $
3 1
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''
