print("Welcome to the secret word game!")
print("I am thinking of a 3 letter word. Can you guess the word?")
secret_word = ("c", "a", "t")
secret_word = sorted(secret_word)
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
        
        
        

        
        
   
    
