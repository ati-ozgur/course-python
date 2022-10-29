
movie1 = [1,"The Shawshank Redemption",1994,9.2]

movie2 = [2,"The Godfather",1972,9.2]

movie_list = [movie1,movie2]


empty_list_of_list = [
		[],
		[]
]

movie_list2 =  [
		[1,"The Shawshank Redemption",1994,9.2],
		[2,"The Godfather",1972,9.2]
]

for movie in movie_list2:
	print(movie)


for movie in movie_list2:
	for info in movie:
		print(f"{info} " ,end="")
	
	print("")