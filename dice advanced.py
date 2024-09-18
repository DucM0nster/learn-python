import random

def versuch():
  wurf = random.randint(1,6)
  print(f"Du hast eine {wurf} gewürfelt.")
  input("drücke Enter zum erneuten Würfeln.")
  versuch()
  
versuch()
  