# python program to check leep year


year = int(input('Enter a year to check leap or not::: '))
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print('leap')
else:
    print('not leap')