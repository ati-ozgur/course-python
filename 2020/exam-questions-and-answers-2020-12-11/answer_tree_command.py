from os import listdir
from os.path import isfile,isdir, join

def print_folders_in_directory(directory_name,indentation_count = 0 ):
	for name in listdir(directory_name):
		# to skip hidden folders, like .git
		if "." == name[0]:
			continue
		fullname = join(directory_name, name)
		if isdir(fullname):
			if indentation_count > 1:
				line =  "____" * indentation_count   + name
			else:
				line = name
			print(line)
			print_folders_in_directory(fullname,indentation_count + 1)




print_folders_in_directory("..")