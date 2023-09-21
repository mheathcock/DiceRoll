import random

def rolldice():
    while True:
         print(random.randrange(1,6))
         input("Roll again?")
         
rolldice()
