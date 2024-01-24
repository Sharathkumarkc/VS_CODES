# python program to convert decimal degree into  degree , minutes and seconds
dd = float(input('Enter decimal degree::: '))
degree = dd//1
temp = (dd % 1)* 60
minutes = temp//1
seconds = (temp% 1)*3600