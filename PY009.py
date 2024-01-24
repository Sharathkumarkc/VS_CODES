# Python program to calculate compound intrest
# logic :: CI = p(1+(r/n))**nt -p

p = int(input('Enter partical amount::: '))
r = float(input('Enter rate of intrest::: '))
n = int (input('enter the number of times the intrest is compounded:::  '))
t = int(input('enter the overall tennure::: '))

ci = (p(1+(n/r))**(n*t) )- p
print(f'compound intrest is {ci}')