# Python program to calculate simple intrest
# logic :: principale ammount * time * rate og intrest/100

p = int(input('Enter principale ammout ::: '))
t = int(input('enetr time is year:::  '))
r = float(input('Enter rate of intrest::: '))

pi = (p*t*r)/100
print(f'simple intrest is {pi}')