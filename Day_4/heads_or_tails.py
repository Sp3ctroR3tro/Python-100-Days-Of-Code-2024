# The following code utilizes the random module to flip a coin
import random

flip_a_coin = True
while True:
    try:
        user_choice = int(input('What is your choice? Enter "0" for Heads or  "1" for Tails? \n'))
        if user_choice == 0:
            print("You have selected Heads")
        elif user_choice == 1:
            print("You have selected Tails")
        else:
            print("This is not a valid choice please select again")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    coin_side = random.randint(0, 1)
    if user_choice == coin_side:
        print(f"You have selected correctly it is {'Heads' if coin_side == 0 else 'Tails'}")
    else:
        print(f"Sorry, the correct choice was {'Heads' if coin_side == 0 else 'Tails'}")

    flip_a_coin = input("Would you like to flip a coin? \nEnter 'Y' for yes or 'N' for no. \n")
    if flip_a_coin != 'Y':
        break
