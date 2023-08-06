import os

file_name = "my_file.txt"

if os.path.exists(file_name):
    print("The file exists.")
else:
    print("The file does not exist.")
