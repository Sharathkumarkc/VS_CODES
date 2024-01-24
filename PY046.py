# Write aprogram to generate mean,median,mode,stdev using statstical module

import statistics as st
data = [1,3,5,7,9,11,13]
# calculating mean
print(st.mean(data))
# checking centerd value in stored list
print(st.median(data))
# Checking repeated value
print(st.mode(data))
# calculating standard devision
print(st.stdev(data))
