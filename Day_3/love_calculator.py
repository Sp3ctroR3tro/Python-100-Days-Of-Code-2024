def calculate_love_score(name1, name2):
    # Count occurrences of letters in "TRUE" and "LOVE" in both names
    true_count = sum(name1.lower().count(char) + name2.lower().count(char) for char in "true")
    love_count = sum(name1.lower().count(char) + name2.lower().count(char) for char in "love")

    # Combine the counts to make a 2-digit number
    love_score = int(str(true_count) + str(love_count))

    return love_score

def main():
    # Prompt for user input
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")

    # Calculate the love score
    score = calculate_love_score(name1, name2)

    # Determine the message based on the love score
    if score < 10 or score > 90:
        message = f"Your score is {score}, you go together like coke and mentos."
    elif 40 <= score <= 50:
        message = f"Your score is {score}, you are alright together."
    else:
        message = f"Your score is {score}."

    print(message)

if __name__ == "__main__":
    main()