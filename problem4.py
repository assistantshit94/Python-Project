import os

# Specify the path to the file you want to read

directory_path = "/"

# List all files in the specified directory

contents = os.listdir(directory_path)

# Print the contents of the directory
for item in contents:
    print(item)