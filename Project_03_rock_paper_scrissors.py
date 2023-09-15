import random 

print("We are goin to play rock paper scissor with computer. Yayyyyy! ")


def play() :
    computer = random.choice(["r", "p", "s"])
    user = input("'r' for rock, 'p' for paper, 's' for scrissor. Enter your choice \n")
    if computer == user :
        return f"It's a tie. Computer's choice was {computer}"
    
    if is_win(user, computer) :
        return f"Yahoooo! You won! Computer's choice was {computer}"
    
    return f"You lost! Computer's choice was {computer}"

# r > s , s > p , p > r

def is_win(user, computer) :
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r") :
        return True
    
    
print(play())