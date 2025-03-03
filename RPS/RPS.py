import random as rd

options = ["rock" , "paper", "scissors"]

for i in range (1,7): #works like a for loop in C Language.

    a = rd.choice(options).lower()

    b = input("Enter your choice: ").lower()

    if a != b:

        if a == "rock" and b == "scissors":
            print("Computer wins")

        elif a == "scissors" and b == "rock":
            print("You win")

        elif a == "paper" and b == "rock":
            print("Computer wins")

        elif a == "rock" and b == "paper":
            print("You win")

        elif a == "scissors" and b == "paper":
            print("Computer wins")

        elif a == "paper" and b == "scissors":
            print("You win")

    else :
        print("It's a draw!")

    print(f"you have {6-i} attempts left") #no. of attempts displayed.
    print(f"computer chose {a}")

