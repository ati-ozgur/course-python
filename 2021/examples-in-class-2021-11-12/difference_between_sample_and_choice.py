from random import choices, sample

def start_deck(card_list):
	# your code should return a 5 numbers list
	return None


card_list = list(range(1,5))

print("choices")
l1 = choices(card_list, k=4)
print(l1)
l1 = choices(card_list, k=4)
print(l1)
l1 = choices(card_list,k=4)
print(l1)
l1 = choices(card_list,k=4)
print(l1)
print("sample")
l1 = sample(card_list,k=4)
print(l1)
l1 = sample(card_list, k=4)
print(l1)
l1 = sample(card_list,k=4)
print(l1)
l1 = sample(card_list,k=4)
print(l1)

