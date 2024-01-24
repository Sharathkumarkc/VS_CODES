# python program to print the smallest element in an array
list2 = [3,6,9,90,7,6,55,34,2,]

small = list2[0]
for number in list2:
    if number < small:
        small = number
print(small)