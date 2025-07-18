import random
import time
import sys

print("Greetings")
time.sleep(0.2)
while True:
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_response = input("Please choose rock, paper, or scissors: ")
        if player_response in choices:
            break
        else:
            print("Type your response")

    print("Rock")
    time.sleep(.5)
    print("Paper")
    time.sleep(.5)
    print("Scissors")
    time.sleep(.5)
    print("SHOOT!")
    time.sleep(2)

    computer_choice = random.choice(choices)
    if player_response == 'rock' and computer_choice == 'scissors' or \
    player_response == 'paper' and computer_choice == 'rock' or \
    player_response == 'scissors' and computer_choice == 'paper':
        print("You Win!")
    else:
        print("You Lose :( ")
    time.sleep(1)
    keep_playing = input("Would you like to play again? (Y/N): ")
    if keep_playing == 'N':
        break 



