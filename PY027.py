# python program to print the duplicate elements of an array

weight = [10,32,54,65,54,10,11,34,32,100,45]
# importing counter module
from collections import Counter
# counting repeated a newlist only with 
d = Counter(weight)
print(d)

nem_list = list([item for item in d if d [item]>1])
print(nem_list)
