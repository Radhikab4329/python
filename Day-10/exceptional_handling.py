import os

folders = input("provide space in between two folder names").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("provide a valid folder name")
        continue

    print("==== listing files of the folder - " + folder)

    for file in files:
        print(file)


