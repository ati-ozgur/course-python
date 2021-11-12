from random import sample

def start_deck(card_list):
	# your code should return a 5 numbers list
	start_cards = []
	start_cards_found = False
	while not start_cards_found:
		l1 = sample(card_list, k=4)
		total = sum(l1)
		if total < 45:
			necessary_card = 45 - total
			if (not necessary_card in l1) and (necessary_card in card_list):
				l1.append(necessary_card)
				start_cards = l1
				start_cards_found = True

	return start_cards


card_list = list(range(1,52))
cards = start_deck(card_list)
print(cards)


