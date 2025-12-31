import random

choices = ["rock", "paper", "scissors"]

result_table = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"}
}

player = 0        
computer = 0     
round = 1

print("Enter rock / paper / scissors")
print("Type exit to stop")

while True:
    print(f"Round {round}")

    player_choice = input("Your choice: ").lower()
    if player_choice == "exit":
        break

    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    outcome = result_table[player_choice][computer_choice]

    if outcome == "win":
        print("You won this round!")
        player += 1
    elif outcome == "lose":
        print("Computer won this round!")
        computer += 1
    else:
        print("It's a tie")

    print("Score:")
    print(f"You: {player} , Computer: {computer}\n")
    round += 1

print("Game Over")
print("Final Score")
print("You: ", player)
print("Computer: ", computer)
