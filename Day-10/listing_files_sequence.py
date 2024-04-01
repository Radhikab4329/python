import os

folders = input("please provide space in between folder names:").split()

for folder in folders:
    files = os.listdir(folder)
    print("==== listing files for the folder - " + folder)

    for file in files:
        print(file)

