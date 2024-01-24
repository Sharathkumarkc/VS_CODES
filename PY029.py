# Write a program to split odd and even number store it in saparate list respectively
age = [10,13,15,18,17,21,25,22,25,31,38,40,44,42,45,12,16,]
oddAge =[]
evenAge = []
for i in age :
    if i %2 == 0:
        evenAge.append(i)
    else:
        oddAge.append(i)
print(oddAge)
print(evenAge)