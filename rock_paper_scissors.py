import random

user_num_wins = 0
sys_num_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    sys_pick = options[random_num] 
    print(f'system picked, {sys_pick}.')

    if user_input == 'rock' and sys_pick == 'scissors':
        print('You won!')
        user_num_wins += 1

    elif user_input == 'paper' and sys_pick == 'rock':
        print('You won!')
        user_num_wins += 1

    elif user_input == 'scissors' and sys_pick == 'paper':
        print('You won!')
        user_num_wins += 1

    else:
        print('You lost!')
        sys_num_wins += 1


print(f'you won {user_num_wins} times.')
print(f'the system won {sys_num_wins} times.')
print('Goodbye!')