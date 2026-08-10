import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    print("\n----- Rock Paper Scissors Game -----")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulations! You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break