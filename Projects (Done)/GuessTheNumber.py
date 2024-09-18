import random

var = random.randint(1,9)
#print(var)

def guess_the_number():    
    while True:
        guessvar = int(input("Guess 1-10: "))
        if guessvar == var:
            print("gratulation, you win")
            break         
        elif guessvar > var:#
            print("too high")   
        else:
            print("too low")         

guess_the_number()