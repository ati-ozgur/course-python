# take a card between 1-10.
#Sum the taken card to total.
#when summation of rolled dices are greater than 21 
#break the program.
# for example, you took following cards, [10,5,7,10,11]

import random

total = 0
while total < 21:
    # simulate of taking a card between 1,10
    card_random = random.randint(1,10) 
    total = total + card_random
    print(total,card_random)




