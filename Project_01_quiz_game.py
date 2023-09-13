print("Welcome to my quiz game.")
answer = input("Do you want to play my quiz game? ")

if answer.lower() != "yes":
    quit()

print("You'll be asked 3 question.So, let's play!")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

result = "You've got " + str(score) + " correct answers! And total " + str((score / 3) * 100) + " %." 
print(result) 
print("Thanks for playing my game. <3")