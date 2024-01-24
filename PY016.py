# Python program to display to multiplication tabel

num = int(input('Enter a number which you want to generate multiplication tabel::: '))

for value in range (1,11):
    print(f'{num}x{value} = {num * value}\n')