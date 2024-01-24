# Program to create a gueesing game
import random
myChoice = int(input('Choose a number between 1 to 5: \n'))
# Declaring choices
cords = [1,2,3,4,5]

SystemChoice = random.choice(cords)
if myChoice == SystemChoice:
    print('correctely guessed the number')
else:
    print(f'system choice is {SystemChoice}')
    print('Wrongaly guessed the number')
