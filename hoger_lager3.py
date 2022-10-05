from random import randint

getal = randint(0,100)
pogingen = 6  

while True:
  geraden = int(input("Raad het getal, je kan nog " + str(pogingen) + " keer proberen:"))
  pogingen = pogingen - 1
  
  if pogingen == 0:
    print("Geen pogingen over! Het getal was " + str(getal))
    break;
  elif getal < geraden:
    print("Lager! 👎")
  elif getal > geraden:
    print("Hoger! 👍")
  elif getal == geraden:
    print("Juist geraden! Proficiat!")
    break
    
    
  