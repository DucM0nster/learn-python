import random
import os
import platform



print("1 = Stone, 2 = Paper, 3 = Scissors")

def SSP():
    var1 = input("1, 2, 3 or 0 to exit ")
    var1 = int(var1)
    if var1 == 1:
        print("Stone")
    if var1 == 2:
        print("Paper")
    if var1 == 3:
        print("Scissors")
    if var1 == 0:
        print("aufgabe")
        exit()

    var2 = random.randint(1, 3)
    if var2 == 1:
        print("Stone")
    if var2 == 2:
        print("Paper")
    if var2 == 3:
        print("Scissors")

    #Gewinnangaben

    #draw
    if var1 == var2:
        print("draw, try again")
    #player wins
    elif (var1 == 1 and var2 == 3) or (var1 == 2 and var2 == 1) or (var1 == 3 and var2 == 2):
        print("player wins")
    #Bot wins
    else:
        print("Bot Wins")
   

def clear():
    current_os = platform.system()
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear') 


def get_input():
    SSP()
    input()
    clear()
    get_input()

get_input()