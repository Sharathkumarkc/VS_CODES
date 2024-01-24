# Pyton program to swap two variables without temporary variable
a = 'juice'
b = 'water'

print('Before swaping')
print(f'a is{a}')
print(f'b is {b}')


a ,b = b , a
print('after swaping using temporary variable')
print(f'a is{a}')
print(f'b is {b}')