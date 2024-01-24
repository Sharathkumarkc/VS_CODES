# Python program to generate a random number
import random
# Declaring variable
num = int(input('Enter total number of rondom number you want to generate:: '))
randomList = []
# Iterating through range of numbers

for i in range(1,num+1):
    rand = random.randint(1,100)
    randomList.append(rand)
print(randomList)