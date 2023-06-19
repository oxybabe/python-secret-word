import random

easy_word_bank = ["cat", "dog", "pie", "time"]
medium_word_bank = ["cherry", "design", "command", "giraffe"]
hard_word_bank = ["association", "vegetarian", "negotiation", "cooperative"]
print("Welcome to the secret word game!")
user_input = input("Select a level: easy, medium, or hard.")
if user_input == "easy":
    secret_word = random.choice(easy_word_bank)
elif user_input == "medium":
    secret_word = random.choice(medium_word_bank)
elif user_input == "hard":
    secret_word = random.choice(hard_word_bank)
print("Can you guess the secret word?")
secret_word = list(secret_word)
# print(secret_word)
guess_list = []
correct = False
while not correct:
    guess = input("Guess a letter between a-z: ")
    guess_list = sorted(guess_list)
    if guess not in secret_word:
        print("You guessed an incorrect letter!")
    elif guess in secret_word:
        guess_list.append(guess) 
        print("You guessed the following correct letters: ", guess_list)
    if set(guess_list) == set(secret_word):
        
        print("Correct! You guessed the secret word! The secret word was", "" .join(secret_word)) 
        correct = True
        break
    # In Python, the set() constructor creates a new set object. The set() constructor takes a list of items as an argument and makes a new set that contains only those items. 