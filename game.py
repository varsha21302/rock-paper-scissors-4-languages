import random
option =("rock","paper","scissors")
running=True

 
while running:

    player = None
    computer=random.choice(option)

    while player not in option:
        player=input("Enter a choice (rock paper scissors):")

        print(f"Player:{player}")
        print(f"Computer:{computer}")


        if player==computer:
         print("It's a tie!")
        elif player=="rock" and computer=="scissors":
            print("You Win!")
        elif player=="paper" and computer=="rock":
            print("You Win!")
        elif player=="scissors" and computer=="paper":
            print("You Win!")
        else:
            print ("You lose!")

        
        play_again = input("Play again? (y/n) : ").lower()
        if not play_again=="y":
            running = False

print("Thanks for playing!!!!!!")            

