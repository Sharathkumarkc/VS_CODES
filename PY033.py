# Write a function to perform simpale calculater using if-elif-else

# Function defination
def calc(num1,num2,operator):
    if operator == 'sum':
        print(num1 + num2)
    elif operator == 'sub':
        print(num1 - num2)
    elif operator == 'prod':
        print(num1 * num2)
    elif operator == 'div':
        print(num1 / num2)
    else:
        print('Enter valid operator')
# calling the function
calc(14,2,'div')