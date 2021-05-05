# import os
# files = os.listdir('.')

# for file in files:
#     print(file)

from os import listdir
from os.path import isfile, join

my_path = "./os_test"
onlyfiles = [file for file in listdir(my_path) if isfile(join(my_path, file)) and not file.endswith('.py')]
print(onlyfiles)