
def say_hi(name):
    name_length = len(name)
    print("Hallo, " + name + "! Dein Name hat " + str(name_length) + " Buchstaben.")
    
say_hi(input("Wie heißt du? "))
