import random

def guest_the_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a random number from 1 to {x}: "))
        if random_number > guess:
            print("Sorry, Wrong guessed number. Too low")
        elif random_number < guess:
            print("Sorry, Wrong guessed number. Too high")

    print(f"Yay! You've guessed the right number {guess}")

guest_the_number(10)
