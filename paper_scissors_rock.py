# imported modules
import random

#variables we are tracking
user_wins = 0
computer_wins = 0
draws = 0
rounds = 0

# variable that stores computers options
options = ['paper', 'scissors', 'rock']

while True:
    #players choice
    player_input = input('Choose paper, scissors, rock or Q to quit: ').lower()
    if player_input == 'q':
        break
    
    if player_input not in options:
        continue
    
    #computers choice selected
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    #going through winning options
    if player_input == 'rock' and computer_pick == 'scissors':
        print('Congratulations! you won!')
        user_wins += 1
        rounds += 1
        
    elif player_input == 'paper' and computer_pick == 'rock':
        print('Congratulations! you won!')
        user_wins += 1
        rounds += 1
    
    elif player_input == 'scissors' and computer_pick == 'paper':
        print('Congratulations! you won!')
        user_wins += 1
        rounds += 1
    
    elif computer_pick == 'rock' and player_input == 'scissors':
        print('Computer won!')
        computer_wins += 1
        rounds += 1
    
    elif computer_pick == 'paper' and player_input == 'rock':
        print('Computer won!')
        computer_wins += 1
        rounds += 1
    
    elif computer_pick == 'scissors' and player_input == 'paper':
        print('Computer won!')
        computer_wins += 1
        rounds += 1
    
    else:
        print('It is a draw! Try again!')
        draws += 1
        rounds += 1
        
print(f'You won {user_wins}, the computer won {computer_wins} times and you had {draws} draws')
print(f'Thank you for playing {rounds} of rounds of paper/scissors/rock. Goodbye!')