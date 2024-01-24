# create 10 folder using OS module

import os
dir = os.getcwd()
print(dir)

for i in range(1,11):
    os.mkdir(f'{dir}/test_{i}')