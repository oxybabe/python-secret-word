import random
print("Welcome to the secret word game!")
print("I am thinking of a 3 letter word. Can you guess the word?")
secret_word = "cat"
guess_list = []
correct = False
while not correct:
    guess = input("Guess a letter between a-z: ")
    if guess == secret_word:
        correct = True
        print("Correct! You guessed the secret word!")
    elif guess not in secret_word:
        print("You guessed an incorrect letter!")
    elif guess in secret_word:
        guess_list.append(guess) 
        print("You guessed the following correct letters: ", guess_list)
    if guess_list == ["c", "a", "t"]:
        print("Correct! You guessed all the correct letters!")
        





