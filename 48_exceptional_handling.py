a=5
b=2

k = int(input("enter a number"))
print(k)

try:
    print('resource open')
    print(a/b)

except ZeroDivisionError as e:
    print('cant divide a number by zero',e)

except ValueError as e:
    print('invalid input')

except Exception as e:
    print('something went wrong')

finally:
    print('resource closed')
