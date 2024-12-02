import random
chance = [ "rock", "paper", "scissor"]
user = (input("please enter rock paper or scissor "))

comp = random.choice(chance)
print("you chose ", user)
print ("comp chose", comp)
if user == "rock" and comp == "scissor" or user == "r" and comp == "scissor":
    print("you won")
elif user == "paper"  and comp == "rock" or user == "p"  and comp == "rock":
    print("you won")
elif user == "scissor" and comp == "paper" or user == "s" and comp == "paper":
    print("you won")
else:
    print ("you lost")    