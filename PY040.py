# python program to print the largest element in an array

list_1 = [3,1,2,4,6,5,8,90,67,1001,43,]

large = 0
for number in list_1:
    if number > large :
        large = number
print(large)