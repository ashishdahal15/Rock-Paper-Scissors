import random

choices = ["Rock", "Paper", "Scissor"]


def the_game():
    user = input("Pick one:\nRock/Paper/Scissor: ").title()

    if user not in choices:
        print("Invalid Entry!")
        return "invalid"

    computer = random.choice(choices)
    print(f"The computer picked: {computer}")

    if (
        (user == "Rock" and computer == "Paper") or
        (user == "Paper" and computer == "Scissor") or
        (user == "Scissor" and computer == "Rock")
    ):
        print("You lost!")
        return "computer"

    elif (
        (user == "Rock" and computer == "Scissor") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissor" and computer == "Paper")
    ):
        print("You won!")
        return "user"

    else:
        print("We both chose the same!")
        return "draw"


user_score = 0
computer_score = 0

next_round = "y"

while next_round == "y":
    winner = the_game()

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    next_round = input("\nDo you want to play again? (Y/N): ").lower()

print("\n========== FINAL SCORE ==========")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You won the match!")
elif computer_score > user_score:
    print("🤖 The computer won the match!")
else:
    print("🤝 The match ended in a draw!")
