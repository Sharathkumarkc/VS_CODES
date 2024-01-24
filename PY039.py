# Write a prgram to convert two list into a dictionary as key value pairs

keys = ['name','addres','age']
values = ['sharath','gundalpet',23]


info = {}
if len(keys) == len(values):
    listlength = len(keys)
    for i in range(listlength):
        info[keys[i]] = values[i]
print(info)