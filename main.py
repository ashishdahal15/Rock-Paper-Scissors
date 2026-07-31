import random
user = input(' Pick one: \n Rock/Paper/Scissor :').title()
list_1 = ['Rock', 'Paper', 'Scissor']
computer = random.choice(list_1)
print('The computer picked: ', computer)
if user == 'Rock' and computer == 'Paper' or user == 'Paper' and computer == 'Scissor' or user == 'Scissor' and computer == 'Rock':
    print('I won!  ')
elif user == 'Rock' and computer == 'Scissor' or user == 'Paper' and computer == 'Rock' or user == 'Scissor' and computer == 'Paper':
    print('You won!')
elif user == computer:
    print('We both chose the same!')
else:
    print("Invalid Entry")
