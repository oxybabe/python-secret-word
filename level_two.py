import random

word_bank = ["cat", "design", "cherry", "time"]
print("Welcome to the secret word game!")
print("Can you guess the secret word?")
secret_word = random.choice(word_bank)
secret_word = list(secret_word)
print(secret_word)
guess_list = []
correct = False
while not correct:
    guess = input("Guess a letter between a-z: ")
    guess_list = sorted(guess_list)
    if guess in secret_word:
        guess_list.append(guess) 
        print("You guessed the following correct letters: ", guess_list)
    elif guess not in secret_word:
        print("You guessed an incorrect letter!")
    if set(guess_list) == set(secret_word):
        print(f"Correct! You guessed the secret word! The secret word was", "" .join(secret_word)) 
        correct = True
        
        





