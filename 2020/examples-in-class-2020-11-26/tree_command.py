from os import listdir
from os.path import isfile,isdir, join

def print_folders_in_directory(directory_name):
	for name in listdir(directory_name):
		fullname = join(directory_name, name)
		if isdir(fullname):
			print(name)


#directory_name = "."


print_folders_in_directory(".")
