import random

def code():
    answer = [random.randint(1, 6) for _ in range(4)]
    return answer

def guess():
    while True:
        print("Enter your guess as a 4-digit number.")
        print("Each digit should be between 1 and 6.")

        addy = input("Enter your guess: ")

        if len(addy) == 4:
            valid = True  # Assume input is valid
            for char in addy:
                if char not in "123456":  # If an invalid digit is found
                    valid = False  # Mark input as invalid
                    break  # Stop checking further

            if valid:
                guess = [int(char) for char in addy]
                break

        print("Invalid input. Please enter 4 digits (each 1-6).")
    
    return guess

def feedback(answer, addy):  
    position = 0
    correct_digit = 0

    answer2 = answer[:]  # Copy of secret_code to track used digits
    addy2 = addy[:]  # Copy of user_guess to track checked positions

    # First pass: Count correct digits in correct positions
    for i in range(4):
        if addy2[i] == answer2[i]:  
            position += 1  
            answer2[i] = None  # Mark as used
            addy2[i] = None  # Mark as used

    # Second pass: Count correct digits in wrong positions
    for i in range(4):
        if addy2[i] is not None and addy2[i] in answer2:
            correct_digit += 1  
            answer2[answer2.index(addy2[i])] = None  # Remove matched digit

    return position, correct_digit  # Return feedback counts

def main_game():
    print("Welcome to Mastermind!")
    secret_code = code()
    max_attempts = 10

    for attempts in range(1, max_attempts + 1):
        addy = guess()
        position, correct_digit = feedback(secret_code, addy)
        print(f"Attempt {attempts}: Correct position = {position}, Correct digit = {correct_digit}")

        if position == 4:
            print("Congratulations! You guessed the code!")
            return

    print(f"Game Over! The correct code was: {''.join(map(str, secret_code))}")  

main_game()
