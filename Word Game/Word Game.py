import random as rd

words=["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Boysenberry", "Cantaloupe", "Cherry", "Clementine", "Cranberry", "Currant", "Date", "Dragon Fruit", "Durian", "Elderberry", "Fig", "Gooseberry", "Grape", "Grapefruit", "Guava", "Honeydew Melon", "Jackfruit", "Kiwi", "Kumquat", "Lemon", "Lime", "Loganberry", "Longan", "Loquat", "Lychee", "Mandarin", "Mango", "Mangosteen", "Melon", "Mulberry", "Nectarine", "Orange", "Papaya", "Passion Fruit", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate", "Prickly Pear", "Quince", "Rambutan", "Raspberry" , "Red Currant", "Star Fruit", "Strawberry", "Tangerine", "Ugli Fruit", "Watermelon"]

answer=rd.choice(words).lower()

#print(answer)

attempts=0
guesses=set()

print("Welcome to the Word Game!")
print("The word is a fruit.")
print("You have 6 Lives.")
print("Good luck!")

#__________________________________________________

def masked_word(answer, guesses):

    masked = ""  # empty string                       

    for letter in answer:       

        if letter in guesses:       

            masked = masked + letter           

        else:                          

            masked = masked + "_"              

    return masked                      

#__________________________________________________

while attempts<6:

    print("Current word:", masked_word(answer, guesses))

    print("Guessed letters:", ' '.join(guesses) if guesses else "None")

    '''
    print() is a built-in Python function that outputs text to the console.
    "Guessed letters:" is a string that serves as a label for the output.
    ' '.join(guesses) is a method that:

    Takes the list guesses
    Joins all the elements of the list into a single string
    Uses a space ' ' as the separator between each guessed letter


    if guesses else "None" is a conditional expression that:

    Checks if the guesses list is non-empty
    If guesses contains elements, it uses ' '.join(guesses)
    If guesses is empty, it uses the string "None"
    
    '''


    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue

    if guess in guesses:  
        print("You already guessed that letter. Try again."  )
        continue  


  
    guesses.add(guess)


    if guess in answer:
        print("Good guess!")
        if masked_word(answer, guesses) == answer:
            print("\nCongratulations! You guessed the word:", answer.capitalize())
            break
    else:
        attempts += 1
        print(f"Incorrect guess. You have {6 - attempts} Lives left.")

if masked_word(answer, guesses) != answer:
    print("\nGame over! The correct word was:", answer.capitalize())
