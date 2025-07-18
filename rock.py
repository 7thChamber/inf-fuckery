import random
import time

print("Greetings,")

while True:
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_response = input("Please choose rock, paper, or scissors: ")
        if player_response in choices:
            break
        else:
            print("Type your response")

    computer_choice = random.choice(choices)
    if player_response == 'rock' and computer_choice == 'scissors' or \
    player_response == 'paper' and computer_choice == 'rock' or \
    player_response == 'scissors' and computer_choice == 'paper':
        print("You Win!")
    else:
        print("You Lose :( ")
    keep_playing = input("Would you like to play again? (Y/N): ")
    if keep_playing == 'N':
        break 



