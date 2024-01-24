# Python program to generate Summation of number between two number

lowervalue = int(input('Enter lower value:::'))
uppervalue = int(input('Enter upper value:::'))
sum = 0
for sum in range(lowervalue,uppervalue+1):
    sum = sum+sum
print(sum)