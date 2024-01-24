# Python program to print the Fibonacci sequenece

stop = int(input('Enter maximum value to stop Fibonacci::'))

a = 0
b = 1
count = 0
while count < stop+1:
    print(a)
    nextvalue = a + b
    a = b
    b = nextvalue
    count = count +1
