# os module

import os

# writens current working directory
dir = os.getcwd()
print(dir)

#os.mkdir('C:\Users\SHARATHKUMAR\OneDrive - MSFT\Documents\VS_CODES/test')
os.mkdir(f'{dir}\ test')