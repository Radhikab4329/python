import os

folders = input("please provide space in between folder names:").split()

    for i in folders:
        files = os.listdir(i)
        print(files)


