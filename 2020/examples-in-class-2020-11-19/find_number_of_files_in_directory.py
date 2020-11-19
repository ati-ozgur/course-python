from os import listdir
from os.path import isfile, join

def print_files_in_directory(directory_name):
	for file in listdir(directory_name):
		if isfile(join(directory_name, file)):
			print(file)

def count_files_in_directory(directory_name):
	count = 0
	for file in listdir(directory_name):
		if isfile(join(directory_name, file)):
			count = count + 1

	return count

# print files in current directory
#print_files_in_directory(".")

# print files in 1 directory above
x = count_files_in_directory("..")
print(f"There are {x} files")
print_files_in_directory("..")
