import os


BASE = os.getcwd()

files_directories_names_list = os.listdir(BASE)

for name in files_directories_names_list:
    if name.endswith(".txt"):
        address = BASE + "/" + name
        os.remove(address)
