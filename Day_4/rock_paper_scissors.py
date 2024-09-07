# The following code allows the user to play rock, paper, scissors against the computer.
import random  # importing the random module

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_score = 0
computer_score = 0
draws = 0

# While loop to run the game
while True:
    try:
        user_choice = int(input("What is your choice? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
        if user_choice < 0 or user_choice > 2:
            raise ValueError("Invalid choice. Please select 0, 1, or 2.")

        print(f"You chose: \n {choices[user_choice]}")

        # Generate the computers choice
        computer_choice = random.randint(0, 2)
        print(f"Computer chose: \n {choices[computer_choice]}")

        # Generate the winner
        if user_choice == computer_choice:
            print("Draw!")
            draws += 1
        elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
            print("You win!")
            user_score += 1
        else:
            print("You lose")
            computer_score += 1
    except ValueError as e:
        print(e)
    # Prompt the user to keep playing
    play_again = input("Would you like to play again? \n Press 'Y' to continue or 'N' to quit. \n")
    if play_again != 'Y':
        break

# Calculating the final score and determining the overall winner.
print(f"The final score was User:{user_score}, Computer:{computer_score}, with {draws} draws.")
if user_score > computer_score:
    print(f"You have won this round of Rock, Paper, Scissors! \nYou are the champion.")
elif user_score == computer_score:
    print(f"You and the computer are currently tied, try again if you want to reign supreme")
else:
    print(f"The computer has defeated you and is the current champion of Rock, Paper, Scissors!")
