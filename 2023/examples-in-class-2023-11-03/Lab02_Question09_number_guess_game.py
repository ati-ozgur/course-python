import random
number = random.randint(0,100)

print("try to guess the number between 0 and 100")

is_number_found = False
while not is_number_found:
    str_guess = input("give your guess: ")
    guess = int(str_guess)
    if guess == number:
        is_number_found = True
        print(f"you have found the number: {number}")
    elif guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("you have entered a number wrong")

