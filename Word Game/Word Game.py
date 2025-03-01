import random as rd

words=["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Boysenberry", "Cantaloupe", "Cherry", "Clementine", "Cranberry", "Currant", "Date", "Dragon Fruit", "Durian", "Elderberry", "Fig", "Gooseberry", "Grape", "Grapefruit", "Guava", "Honeydew Melon", "Jackfruit", "Kiwi", "Kumquat", "Lemon", "Lime", "Loganberry", "Longan", "Loquat", "Lychee", "Mandarin", "Mango", "Mangosteen", "Melon", "Mulberry", "Nectarine", "Orange", "Papaya", "Passion Fruit", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate", "Prickly Pear", "Quince", "Rambutan", "Raspberry" , "Red Currant", "Star Fruit", "Strawberry", "Tangerine", "Ugli Fruit", "Watermelon"]

answer=rd.choice(words).lower()

#print(answer)

attempts=0
guesses=set()

print("Welcome to the Word Game!")
print("The word is a fruit.")
print("You have 6 attempts to guess the word.")
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
        print(f"Incorrect guess. You have {6 - attempts} attempts left.")

if masked_word(answer, guesses) != answer:
    print("\nGame over! The correct word was:", answer.capitalize())
