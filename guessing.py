import random
n = random.randint(1, 1000)

print("Welcome to GUESS THE NUMBER game ! ")
print("\n")
guess = int(input('Guess the number between 1 to 1000 :'))
guess_token = 0
while True:
    if guess < n:
        print ("Higher")
        guess = int(input("Enter an integer from 1 to 1000: "))
        guess_token += 1
    elif guess > n:
        print ("Lower")
        guess = int(input("Enter an integer from 1 to 1000: "))
        guess_token += 1
    else:
        print("\n")
        print (f"Perfect ! you guessed the number in  -> {guess_token} attempts !  --------------")
        print("\n")
        break

print("Thank you for playing ! ")
print("A program by @sudeepbogati7 ")

