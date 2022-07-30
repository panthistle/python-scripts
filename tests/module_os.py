
import os

# display os commands
#print(dir(os))

# get current directory
curDir = os.getcwd()
print(curDir)

# change directory (using absolute or relative path)
os.chdir('../')
newDir = os.getcwd()
print(newDir)

# list files/directories in current directory
print(os.listdir())
# create directory inside current directory
os.mkdir('New Folder')
os.makedirs('NewTopFolder/NewSubFolder')
print(os.listdir())
# remove directories
os.rmdir('New Folder')
os.removedirs('NewTopFolder/NewSubFolder')
print(os.listdir())

# remove text file
if os.path.exists("NewTestFile.txt"):
 	os.remove("NewTestFile.txt")

# create text file
f = open('NewTestFile.txt', 'w')
f.close()
print(os.listdir())

# rename files/directories
os.rename('NewTestFile.txt', 'NewTmpFile.txt')
# get file information
print(os.stat('NewTmpFile.txt'))
print(os.listdir())

# remove text file
if os.path.exists("NewTmpFile.txt"):
 	os.remove("NewTmpFile.txt")

# walk through all dirs and files down a path
for dirpath, dirnames, filenames in os.walk(newDir):
	print('Current path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
	print()

# get environment variables
print(os.environ.get('USER'))

# # safe way to join paths
# #os.path.join(newDir, 'test.txt')

# # os.path useful properties
# #print(os.path.basename('/tmp/text.txt'))
# #print(os.path.dirname('/tmp/text.txt'))
# #print(os.path.split('/tmp/text.txt'))
# #print(os.path.exists('/tmp/text.txt'))
# #print(os.path.isdir('/tmp/text.txt'))
# #print(os.path.isfile('/tmp/text.txt'))
# #print(os.path.splitext('/tmp/text.txt'))

# change back
os.chdir(curDir)
print(os.getcwd())
