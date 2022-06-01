
import os

# change current directory
os.chdir('./files_test_rename')

# check directory
print(os.getcwd())

# rename multiple files
newPrefix = 'Item'
sep = '_'
for f in os.listdir():
    prefix, suffix = f.split(sep)
    print(prefix, ', ', suffix)
    newName = newPrefix + sep + suffix
    os.rename(f, newName)
