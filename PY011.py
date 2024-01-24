# python program to check BMI
# BMI = mass(kg)/height^2(m)

name = input('Enter a name:: ')
weight = float(input('Enter weight in kg :::'))
height = float(input('Enter height in meter ::: '))

bmi = weight/(height*height)
print(f'bmi value of {name} is bmi')
if bmi < 18.49:
    print(f'{name} is underweight')
elif bmi >=18.49 and bmi < 24.99:
    print(f'{name} is normal weight')
elif bmi >= 24.99 and bmi < 29.99:
    print(f'{name} is overweight')
else:
    print(f'{name} is obese') 