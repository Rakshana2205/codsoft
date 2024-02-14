import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
        
        try:
            user_choice_index = int(input("Enter your choice (1-4): "))
            
            if user_choice_index == 4:
                print("\nThanks for playing!")
                break

            if user_choice_index not in range(1, 4):
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue

            user_choice = choices[user_choice_index - 1]
            computer_choice = random.choice(choices)

            result = determine_winner(user_choice, computer_choice)
            display_result(user_choice, computer_choice, result)

            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1

            print(f"\nYour Score: {user_score}  Computer Score: {computer_score}")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()