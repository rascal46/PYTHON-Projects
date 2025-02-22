import random as rd

print("Welcome to the number guessing game!")

print("I'm thinking of a number between 1 and 100")

print("If you can guess the number in 6 attempts, you win!")

print("Good luck!")

#initializing everything

secret= rd.randint(8,67)

attempts = 0

user_guess = 0

while attempts < 6: # restricting attempts to 6

        try:

            user_guess = int(input("Enter your guess: "))

            attempts = attempts + 1

            z = abs(secret - user_guess) #for absolute value of z and avoiding all the cases.
                                         # this is useful for the user

            if user_guess < secret:
                if z <= 10:
                    print("Just a little higher! Try again.")
                else:
                    print("Went too low! Try again.")

            elif user_guess > secret:
                if z <= 10:
                    print("Just a little lower! Try again.")
                else:
                    print("Went too high! Try again.")
    
            else:  
                print(f"Congratulations! You guessed the number in {attempts} attempts.")  
                break #ends the program if user correctly guesses

        #error management
        except ValueError:  
            print("Invalid input! Please enter a valid number.")
    
           

if attempts == 6:

    print(f"You have run out of attempts! The number was {secret}.") #using f-strings to put the values in the string

print("Game over!")
    
    
