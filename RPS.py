import random

user_wins = 0
user_losses = 0
c_plays = ("paper", "scissors", "rock")

name = input("Let's play! What is your name?\n")

print("\n\n\n\n\n\n\n\n\n\n\n\n\nHey {0}, Ready for a game of Rock, Paper, Scissors? \nBest 3 out of 5 wins!".format(name))


while user_wins < 3 and user_losses < 3:
    print("\n\nWINS : {0} " "  " " LOSSES : {1} ".format(user_wins, user_losses))
    u_plays = str(input("\n\nPaper, Scissors, or Rock?\n\n"))
    u_plays = u_plays.casefold()
    cpu_plays = random.choice(c_plays)
    print("\n... ... ... ... ... \n\n")
    if u_plays not in c_plays:
        print("Check your spelling! Try Again.")
    elif u_plays == cpu_plays:
        print("It's a tie! Let's try again")
    elif u_plays == "rock" and cpu_plays == "scissors":
        print("Rock smashes Scissors! You win!")
        user_wins += 1
    elif u_plays == "scissors" and cpu_plays == "paper":
        print("Scissors cut Paper! You win!")
        user_wins += 1 
    elif u_plays == "paper" and cpu_plays == "rock":
        print("Paper covers Rock! You win!")
        user_wins += 1
    elif u_plays == "rock" and cpu_plays == "paper":
        print("Oh no! Paper covers Rock! You lose.")
        user_losses += 1
    elif u_plays == "scissors" and cpu_plays == "rock":
        print("Oh no! Rock crushes your Scissors. You lose.")          
        user_losses += 1
    elif u_plays == "paper" and cpu_plays == "scissors":
        print("Oh no! Scissors chopped your paper to shreds. You lose")
        user_losses += 1
    else:
        print("Something went wrong. Start again.")       

        
if user_wins == 3:
    print("\n\nWINS : {0} " "  " " LOSSES : {1} ".format(user_wins, user_losses))
    print("\n\nCongratulations! You're the champion.")

elif user_losses == 3:
    print("\n\nWINS : {0} " "  " " LOSSES : {1} ".format(user_wins, user_losses))
    print("\n\nToo Bad. The computer beat you fair and square.")    
else:    
    print("Something went wrong, Let's load this again."