import os


BASE = os.getcwd()
print("I'm hrer:", BASE)

files_directories_names_list = os.listdir(BASE)
print(files_directories_names_list)

full_directories = []
for name in files_directories_names_list:
    full_directories.append(BASE + "/" + name)

print(full_directories)
print()