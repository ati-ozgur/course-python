def create_list_three_four_twelve(max_number):
	pass

l1 = create_list_three_four_twelve(20)	
assert l1 == [1, 2, 'three', 'four', 5, 'three', 7, 
		'four', 'three', 10, 11, 'twelve', 13, 14, 
		'three', 'four', 17, 'three', 19, 'four']


l2 = create_list_three_four_twelve(100)
assert l2 == [1, 2, 'three', 'four', 5, 'three', 7, 
		'four', 'three', 10, 11, 'twelve', 13, 14, 
		'three', 'four', 17, 'three', 19, 'four', 
		'three', 22, 23, 'twelve', 25, 26, 'three', 
		'four', 29, 'three', 31, 'four', 'three', 
		34, 35, 'twelve', 37, 38, 'three', 'four', 
		41, 'three', 43, 'four', 'three', 46, 47, 
		'twelve', 49, 50, 'three', 'four', 53, 
		'three', 55, 'four', 'three', 58, 59, 
		'twelve', 61, 62, 'three', 'four', 65, 
		'three', 67, 'four', 'three', 70, 71, 
		'twelve', 73, 74, 'three', 'four', 77, 'three',
		 79, 'four', 'three', 82, 83, 'twelve', 85, 
		 86, 'three', 'four', 89, 'three', 91, 'four', 
		 'three', 94, 95, 'twelve', 97, 98, 'three', 'four']


