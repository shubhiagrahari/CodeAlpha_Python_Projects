import random

def play_hangman():
    # 5 predefined words
    words = ["python", "intern", "script", "coding", "alpha"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Create the display word with guessed letters and underscores
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
                
        print(f"\nWord: {display}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Win condition
        if "_" not in display:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
            
        # Get user input
        guess = input("Guess a single letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
            
        # Add to guessed list
        guessed_letters.append(guess)
        
        # Check if guess is wrong
        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
        else:
            print(f"Good job! '{guess}' is in the word.")
            
    # Lose condition
    if incorrect_guesses == max_incorrect:
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()