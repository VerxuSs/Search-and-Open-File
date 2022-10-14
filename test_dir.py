import os
import subprocess

flag = 0
paths = []
filename_search = input("Which file : ")
folder_path = input("From where (path) : ")
if not folder_path:
    folder_path = subprocess.check_output('chdir', shell = True, universal_newlines=True)
    print("folder : ", folder_path)
for path, dirs, files in os.walk(str(folder_path).strip()):
    for filename in files:
        if filename_search.upper() in filename.upper():
            flag = 1
            path_file = path
            path_file = path_file + "\\" + filename
            paths.append(path_file)
if flag == 1:
    print("Founded from this paths : ")
    i = 0
    if len(paths) > 1:
        for path in paths:
            i += 1
            print(i, "-", path, "\n")
        num = input("Which file do you want to open (just do enter if you want to exit)")
        file = paths[int(num)-1]
        root, extension = os.path.splitext(file)
        if num != "":
            subprocess.check_call(('start', "", "/max", file), shell = True)
            print("Open")
    else:
        file = paths[0]
        print(paths[0])
        ouvrir = input("Do you want to open it : [Y/n]")
        if ouvrir == "Y" or ouvrir == "y" or ouvrir == "":
            subprocess.check_call(('start', "", "/max", file), shell = True)
            print("Open")
        else:
            print("Not Open")
else:
    print("Inexistent File")
