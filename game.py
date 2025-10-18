import random
#import time
import os

# Clear console for better readability
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the game intro
def print_intro():
    print("🪨  🧻  ✂️  Welcome to Rock, Paper, Scissors!")
    print("Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("----------------------------------------")

# Get player's choice with input validation
def get_player_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

# Get computer's random choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "player"
    else:
        return "computer"

# Display the round result
def display_result(player, computer, winner):
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    if winner == "draw":
        print("Result: It's a draw!")
    elif winner == "player":
        print("Result: You win! 🎉")
    else:
        print("Result: You lose! 💻")

# Ask if user wants to play again
def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    return choice in ['yes', 'y']

# Main game loop
def main():
    player_score = 0
    computer_score = 0
    round_number = 1

    clear_screen()
    print_intro()

    while True:
        print(f"\n------ Round {round_number} ------")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, winner)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores => You: {player_score} | Computer: {computer_score}")

        round_number += 1

        if not play_again():
            print("\nFinal Scores:")
            print(f"You: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("🏆 You are the overall winner!")
            elif player_score < computer_score:
                print("💻 Computer wins the game!")
            else:
                print("🤝 It's a tie overall!")
            print("Thanks for playing! 👋")
            break
        else:
            clear_screen()
            print_intro()

if __name__ == "__main__":
    main()
