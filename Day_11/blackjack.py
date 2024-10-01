from random import randint

# Constants
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21
DEALER_STAND = 17
INITIAL_HAND_SIZE = 2


# Function to draw if the option is available
def draw_card():
    return CARDS[randint(0 ,len(CARDS)-1)]

# Calculate the score of the player and dealers hands
def calculate_hand_value(hand):
    score = sum(hand)
    if score > BLACKJACK and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

# Determine a winner between the player and dealer
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > BLACKJACK:
        return "Player Bust. You lose."
    elif dealer_value > BLACKJACK:
        return "Dealer Bust. You win!"
    elif player_value == dealer_value:
        return "Draw"
    elif player_value == BLACKJACK:
        return "Blackjack! You win!"
    elif dealer_value == BLACKJACK:
        return "Dealer Blackjack. You lose."
    elif player_value > dealer_value:
        return "You win!"
    else:
        return "You lose."



# Prompt to draw another card for the user
def hit_me():
    return input("Would you like another card? \nEnter 'y' to draw another card, 'n' to pass: ").lower()




while True:
    play_game = input("Do you want to play a game of Blackjack? Enter 'y' or 'n': ")
    if play_game.lower() == "n":
        break

    player_hand = [draw_card() for i in range(INITIAL_HAND_SIZE)]
    dealer_hand = [draw_card() for j in range(INITIAL_HAND_SIZE)]

    print("Dealing...")
    print(f"Player hand: {player_hand}, current hand value: {calculate_hand_value(player_hand)}")
    print(f"Dealer hand: {dealer_hand[0]}")

    player_value = calculate_hand_value(player_hand)
    while True:
        draw_again = hit_me()
        if draw_again == "y":
            player_hand.append(draw_card())
            player_value = calculate_hand_value(player_hand)
            print(f"Player's cards:{player_hand}, current hand value: {calculate_hand_value(player_hand)}")
            if player_value == BLACKJACK:
                print("Blackjack! You win!")
                break
            elif player_value > BLACKJACK:
                print("Bust! You lose")
                break
        else:
            break


    # Dealer's Turn, reveal second card
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's cards: {dealer_hand}, current hand value: {dealer_value}")

    # If there are is no Blackjack, or Bust by player, let dealer play
    if player_value < BLACKJACK:
        while dealer_value < DEALER_STAND:
            dealer_hand.append(draw_card())
            dealer_value = calculate_hand_value(dealer_hand)
            print(f"Dealer's cards: {dealer_hand}, current hand value: {dealer_value}")

        result = determine_winner(player_hand, dealer_hand)
        print(result)


