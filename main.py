import random

list_1 = ['Rock', 'Paper', 'Scissor']


def the_game():
    user = input(' Pick one: \n Rock/Paper/Scissor :').title()

    if user not in list_1:
        print('Invalid Entry!')
    else:
        computer = random.choice(list_1)
        print('The computer picked: ', computer)

        if (
            (user == 'Rock' and computer == 'Paper') or
            (user == 'Paper' and computer == 'Scissor') or
            (user == 'Scissor' and computer == 'Rock')
        ):
            print('You lost!  ')

        elif (
            (user == 'Rock' and computer == 'Scissor') or
            (user == 'Paper' and computer == 'Rock') or
            (user == 'Scissor' and computer == 'Paper')
        ):
            print('You won!')
        elif user == computer:
            print('We both chose the same!')


next_round = 'y'
while next_round == 'y':
    the_game()
    next_round = input('Do you want to play the game again?:(Y/N):  ').lower()
