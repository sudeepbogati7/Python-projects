import random
while True:
    choices = ["scissor", "paper", "rock"]
    computer = random.choice(choices)
    player = None

    while player not in choices :
        player = input("scissor / paper / rock ?? :  ").lower()


    if player == computer :
        print("Computer : ", computer)
        print("Player : ", player)
        print("Tie !! ")
    elif player == "scissor":
        if computer == "paper":
            print("Computer ", computer )
            print("Player : ", player)
            print("Congratulation , you win !! ")
        elif computer == "rock":
            print("Computer ", computer)
            print("Player : ", player)
            print("Oh no , you lose  !! ")


    elif player == "paper":
        if computer == "scissor":
            print("Computer ", computer )
            print("Player : ", player)
            print("Ohhh no , you lose  !! ")
        elif computer == "rock":
            print("Computer ", computer)
            print("Player : ", player)
            print("Congaratulation , you win !! ")


    elif player == "rock":
        if computer == "scissor":
            print("Computer ", computer )
            print("Player : ", player)
            print("Congratulation , you win !! ")
        elif computer == "paper":
            print("Computer ", computer)
            print("Player : ", player)
            print("Oh no , you lose  !! ")

    print("\n")
    play_again = input("Play again ? (yes/no) :  ").lower()
    if play_again != "yes":
        break

print("\n Bye ! Thanks for playing | ")
