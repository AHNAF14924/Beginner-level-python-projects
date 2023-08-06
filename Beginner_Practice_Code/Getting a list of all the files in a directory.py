import os

directory = "my_directory"

files = os.listdir(directory)

for file in files:
    print(file)
