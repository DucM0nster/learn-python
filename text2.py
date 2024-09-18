phrase = "Wasser"

print(phrase + " ist net so lecker")

print(phrase.lower())  #lower case
print(phrase.isupper())  #isupper case false

print(phrase.upper())  #upper case
print(phrase.isupper())  #isupper case true

#convert to upper
print(phrase.upper().isupper())

print("Wasser\nist net so lecker")
print("Wasser\"ist net so lecker")
# print("Kot\ist net so lecker") die Fehlermeldung ist fürn Arsch

#Länge bestimmen
print(len(phrase))

print(phrase[0])
print(phrase[2])

#I can grab the Letter
#0 = 1st
#1 = 2nd
#...

print(phrase.index("W"))
print(phrase.index("r"))
print(phrase.index("Wasser"))
print(phrase.index("se"))

# print(phrase.index("xyz"))

print(phrase.replace("o", "ur"))
print(phrase.replace("Wasser", "Eis"))

