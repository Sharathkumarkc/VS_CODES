# Write a program to ask user to input 5 name and store it in a list

totalitem = int(input('Enter total item you want to purchase::'))
itemlist =[]
for item in range (totalitem):
    itemname = input('Enter item {item + 1} name::')
    itemlist.append(itemname)
print(itemlist)