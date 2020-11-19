from os import listdir
from os.path import isfile,isdir, join


def print_files_in_directories_recursively(directory_name):
	for name in listdir(directory_name):
		fullname = join(directory_name, name)
		if isfile(fullname):
			print(name)
		elif isdir(fullname):
			print_files_in_directories_recursively(fullname)


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


if __name__ == "__main__":
	# print files in current directory
	#print_files_in_directory(".")

	# print files in 1 directory above
	x = count_files_in_directory("..")
	print(f"There are {x} files")
	print_files_in_directory("..")
