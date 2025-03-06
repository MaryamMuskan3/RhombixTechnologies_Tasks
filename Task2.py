import random

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

words = ["apple", "banana", "grape", "orange", "mango",  
         "tiger", "lion", "zebra", "horse", "cat",  
         "table", "chair", "pencil", "book", "clock"]

def play_hangman():
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6  
    guessed_letters = []

    print("\nWelcome to Hangman Game!")

    while attempts > 0 and "_" in guessed_word:
        print(hangman_stages[6 - attempts]) 
        print("\nWord:", " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1  

        guessed_letters.append(guess)

 
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(hangman_stages[6])  
        print("\n❌ Game Over! The correct word was:", word)


while True:
    play_hangman()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break