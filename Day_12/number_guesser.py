import random



def select_difficulty(difficulty):
    lives = 10
    if difficulty.lower() == "easy":
        lives = 10
        print("You have 10 attempts to guess the number.")
    elif difficulty.lower() == "hard":
        lives = 5
        print("You have 5 attempts to guess the number.")
    else:
        print("Invalid option selected. Setting to default (easy mode) with 10 attempts.")
    return lives

while True:
    game_difficulty= input("Welcome to the Number Guesser Game! \nI'm thinking of a number between 1 and 100. \nChoose a difficulty. Enter 'easy' or 'hard':")
    lives = select_difficulty(game_difficulty)
    WINNING_NUMBER = random.randint(1, 100)

    while lives > 0:
        try:
            user_guess = int(input("Make a guess: "))
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer")
            continue

        if user_guess == WINNING_NUMBER:
                print(f"You got it! The number was {WINNING_NUMBER}")
                break
        elif user_guess > WINNING_NUMBER:
            print("Too high. Guess again.")
        else:
            print("Too low. Guess again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")

    if lives == 0:
        print(f"Game over, the number was {WINNING_NUMBER}")


    play_again = input("Would you like to play again? Enter 'y' for yes or 'n' for no.").strip().lower()
    if play_again == 'n':
        break