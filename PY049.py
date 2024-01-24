# list all folder in current directory and delete it using OS module

import os
dir = os.getcwd()
list_dir = os.listdir(dir)

for i in list_dir:
    if i.startswith('Test'):
        try:
            os,rmdir(i)