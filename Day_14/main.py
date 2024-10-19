from game_data import data
from art import vs, logo
import random
import os
import platform

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def clear_screen():
    # For Windows
    if platform.system() == "Windows":
        os.system("cls")
    # For Unix-based systems(Linux, MacOS)
    else:
        os.system("clear")


score = 0
keep_playing = True

# Generating the random questions
account_a = random.choice(data)
account_b = random.choice(data)

# Ensuring that the choices will never be the same
while account_a == account_b:
    account_b = random.choice(data)

# Main game logic
while keep_playing:
    clear_screen()
    print(logo)
    print(f"Compare A: {format_data(account_a)} \n{vs} \nCompare B: {format_data(account_b)}")

    # Gather user input for guess
    guess = input("Who has more followers type 'A' or 'B': ").lower()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # Checking to see if the user choice is correct
    is_correct = check_answer(guess, a_followers, b_followers)

    # Feedback section
    if is_correct:
        score += 1
        print(f"Correct! Current Score {score}")
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
    else:
        keep_playing = False
        print(f"Incorrect! Game over, your final score is {score}")
