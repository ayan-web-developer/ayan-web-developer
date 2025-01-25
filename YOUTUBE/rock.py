import random
choice=("rock , paper ,scissor")
user=input("choose rock , paper ,scissor:").lower()
computer=random.choice(choice)
print(f"you chose: {user}")
print(F"computer chose: {computer}")
if user == computer:
    print("It's a tie")
elif(user == "rock" and computer=="scissor") or\
    (user == "scissors" and computer =="paper") or\
    (user == "paper" and computer == "rock"):
    print("You win")
else:
    print("COMPUTER WINS")