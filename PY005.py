# Python program to check if number is positive,negtive or zero
#  logic if a > 0 = positive, if a < 0 = negitive , if a = 0 zero

value = float(input('Enter the value::: '))
if value > 0:
    print(f'{value} is positive number')
elif value < 0 :
    print(f'{value} is negitive nimber')
else:
    print(f'{value} is zero')