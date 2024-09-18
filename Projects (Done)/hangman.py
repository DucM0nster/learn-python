import random

def hangman_display(attempts):
    stages = [
    """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |     / \\
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |     / 
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |     
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |     \|/
        |      
        |     
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |     \|
        |      
        |     
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |      |
        |      
        |     
        _
    """
    ,
     """
        --------
        |      |
        |      O
        |     
        |      
        |     
        _
    """
    ,
     """
        --------
        |      |
        |      
        |     
        |      
        |     
        _
    """
    
    ]
    return stages[attempts]

def hangman():
    words = ["philip", "isst", "fritierte", "snickers"]

    word = random.choice(words)
    print(word)

    guessed_word = "_" * len(word)
    guessed_letters = []
    attempts = 7

    #print(Let's guess!)

    while attempts > 0:
        print(hangman_display(attempts))
        print(f"Erratenes Wort: {guessed_word}")
        print(f"Noch {attempts} Versuche übrig")

        guess = input("letter: ").lower()

        if guess in guessed_letters:
            print("bereits getippt")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Gut geraten '{guess}' ")
            
            guessed_word = "".join([guess if word[i] == guess else guessed_word[i] for i in range(len(word))])
            
        else:
            print(f"'{guess}' isn't in the word")
            attempts -= 1

        if guessed_word == word:
            print(f"you guessed your word'{word}'")
            break
        else:
            print(hangman_display(attempts))
            print(f"you loose. word '{word}'")

hangman()