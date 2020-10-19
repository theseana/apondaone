import os


BASE = os.getcwd()

files_directories_names_list = os.listdir(BASE)

full_directories = []
for name in files_directories_names_list:
    if name.endswith(".txt"):
        address = BASE + "/" + name
        full_directories.append(address)

for file in full_directories:
    os.remove(file)