# Callculating distance between two geographical coordinates

from math import radians,cos,sin,asin,sqrt,pi


source = (12.31447,76.646728)
destination =(26.174387004022226, 91.70286580517384)

lat1 = source[0]*(pi/100)
lat2 = destination[0]*(pi/100)

long1 = source[1]*(pi/100)
long2 = destination[2]*(pi/100)

dlat = lat2 -lat1
dlong = long2 - long1

a = sin(dlat/2)**2 +cos(lat1) * cos(lat2)


