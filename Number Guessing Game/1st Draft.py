import random as rd

#this was the initial draft. it lacked:
    #1. attempts restriction
    #2. error management
    #3. Hint to user
    #4. Proper Instruction Displays

secret= rd.randint(1,100)

attempts = 0

guess = False

#print()

while not guessed_correctly:  

    a= int(input("Enter your guess: ") )

    attempts = attempts + 1

    If a < secret then  
        print("Too low! Try again.")

    Else if a > secret then  
        print("Too high! Try again.")
