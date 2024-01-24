# Write a program to identify mataching values between two list

group_A = ['sharath','sumantha','sanjay','manoj']
group_B = ['sanjay','shiva','sagar']
common = []
for i in group_A:
    if i in group_B:
        common.append(i)

print(common)