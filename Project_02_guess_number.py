import random

def guest_the_number(x) :
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a random number from 1 to {x}: "))
        if random_number > guess:
            print("Sorry, Wrong guessed number. Too low")
        elif random_number < guess:
            print("Sorry, Wrong guessed number. Too high")

    print(f"Yay! You've guessed the right number {guess}")

def computer_guess_number(x) :
    low = 1
    high = x
    feedback = ""
    
    while feedback != "c" :
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f"The guessed number is {guess}. If it is Low then enter (L) and if it is High then enter (H) and if it is correct then enter (C) ").lower()
        if feedback == "h" :
            guess = guess - 1
        elif feedback == "l" :
            guess = guess + 1
    
    print(f"Yay! The computer guessed the number correctly!")


# guest_the_number(10)
computer_guess_number(50)
