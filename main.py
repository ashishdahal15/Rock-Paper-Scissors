import random
user = input(' Pick one: \n Rock/Paper/Scissor :').title()
list_1 = ['Rock', 'Paper', 'Scissor']
computer = random.choice(list_1)
print('The computer picked: ', computer)
if user == 'Rock' and computer == 'Paper':
    print('I won! Let me cover your rock! ')
elif user == 'Rock' and computer == 'Scissor':
    print('You won! Hit my Scissors!')
elif user == 'Paper' and computer == 'Rock':
    print('You won! Cover my Rock!')
elif user == 'Paper' and computer == 'Scissor':
    print('I won! Let me cut through you!')
elif user == 'Scissor' and computer == 'Rock':
    print('I won! Let me hit your scissor!')
elif user == 'Scissor' and computer == 'Paper':
    print('You won! Cut my paper!')
elif user == computer:
    print('We both chose the same!')
else:
    print("Invalid Entry")
