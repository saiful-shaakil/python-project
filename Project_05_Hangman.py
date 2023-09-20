import random
from words import words

def display_word(word, guessed_letters) :
    display = ""
    for letter in word :
        if letter in guessed_letters :
            display += letter
        else:
            display += "_"
    
    return display

def hangman() :
    print("Welcome to Hangman!")
    attempts_left = 6
    guessed_letters = []
    secret_word = random.choice(words)
    while attempts_left > 0 :
        print(f"Word: {display_word(secret_word, guessed_letters)}")
        print(f"{attempts_left} attempts remaining.")
        input_letter = input("Enter letter: ").lower()
        
        if len(input_letter) != 1 or not input_letter.isalpha() :
             print("Please enter a valid letter!")
             continue
        
        if input_letter in guessed_letters :
            print("You've already guessed the letter")
            continue 
    
        guessed_letters.append(input_letter)
        
        if input_letter not in secret_word :
            print("Your guess is not correct!")
            attempts_left -= 1
            
        if set(secret_word) <= set(guessed_letters) :
            print(f"Congrats! You've won this game. Secret word {secret_word}")
            break
    else :
        print("You've lost!")
    
hangman()
    