# Creating a program to check Euclidean distance between consecutive points

coordinates1 = (1,2)
coordinates2 = (8,9)

x1 = coordinates1[0]
x2 = coordinates2[0]
y1 = coordinates1[1]
y2 =coordinates2[1]
diff_x =  (x2 -x1)**2
diff_y = (y2 - y1)**2

distance = (diff_x + diff_y)**0.5
print(distance)