from os import listdir
from os.path import isfile,isdir, join

def print_folders_in_directory(directory_name):
	for name in listdir(directory_name):
		# to skip hidden folders, like .git
		if "." == name[0]:
			continue
		fullname = join(directory_name, name)
		if isdir(fullname):
			print(name)
			print_folders_in_directory(fullname)


#directory_name = "."


print_folders_in_directory(".")


#print_folders_in_directory("2020")
#print_folders_in_directory("2020/examples-in-class-2020-11-19")
