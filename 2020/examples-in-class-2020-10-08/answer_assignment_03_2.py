


def character_pyramid(row , ch):
	for i in range(row+1):
		print(ch * i)

#character_pyramid(5,"o")
#character_pyramid(5,"x")

row_str = input("Please enter number of rows: ")
row= int(row_str)

ch = input("please enter a character: ")


character_pyramid(row,ch)