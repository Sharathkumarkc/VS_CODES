# python program to find UTM zone of lat long value
# utm = 31+long/6

lat = 12.36
long = 76.36

if long > 0 and lat > 0:
    print('north and eastern hemispher')
    utmgrid = "N"
elif long > 0 and lat < 0 :
    print('south and eastern hemispher')
    utmgrid = 'S'
elif long < 0 and lat >0:
    print('north and western hemispher')
    utmgrid = 'n'
elif long <0 and lat <0:
    print('south and westren hemispher')
    utmgrid = 's'
elif long = 0 and lat = 0:
    print('primemerdian and equator intersection point')
else:
    print('invalid point')
zone 31 +(long/6)
print(f'Utm zone'{utmgrid})