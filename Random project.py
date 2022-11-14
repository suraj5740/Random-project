import random
repeat=True
while repeat:
    print(random.randrange(1,7))
    next_roll=input("Want to roll dice again?= ")
    if next_roll.lower()=="yes":
        continue
    else: 
        break
        
