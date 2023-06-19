import random
guesses_remaining = 15
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
print(secret_word)
guess_list = []
correct = False
while not correct and guesses_remaining > 0:
    guess = input("Guess a letter between a-z: ")
    guess_list = sorted(guess_list)
    guesses_remaining -= 1
    if guess not in secret_word:
        print("You guessed an incorrect letter!")
        print("You have {} tries remaining.".format(guesses_remaining))
    elif guess in secret_word:
        guess_list.append(guess) 
        print("You guessed the following correct letters: ", guess_list)
        print("You have {} tries remaining.".format(guesses_remaining))
    if set(guess_list) == set(secret_word):
        print("Correct! You guessed the secret word! The secret word was", "" .join(secret_word)) 
        guesses_remaining = 0
        correct = True
        break
    if guesses_remaining == 0 and not correct:
        print("You are out of tries. The correct word was", "" .join(secret_word))