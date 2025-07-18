import random
import time

the_number = random.randint(1, 10)
start_game = input("Guess a number between 1 and 10: ")

while start_game == "":
    print("Please type a number")
    start_game = input("Guess a number between 1 and 10: ")

if start_game == the_number:
    print("You Win!")
else:
    print("Wrong, dumbass.")
    print("The correct number was" +" "+str(the_number))
time.sleep(10)