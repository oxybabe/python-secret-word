import random

word_bank = ["cat", "design", "cherry", "time", "insure", "harmony", "firefighter", "researcher", "dictionary"]
print("Welcome to the secret word game!")
print("Can you guess the secret word?")
secret_word = random.choices(word_bank, k=1)
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
    if guess_list == secret_word:
        print("Correct! You guessed the secret word!") 
        correct = True
        
        





