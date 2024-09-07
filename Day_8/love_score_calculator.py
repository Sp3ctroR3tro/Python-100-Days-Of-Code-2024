def love_score(name_1, name_2):

    # Count occurrences of letters in "TRUE" and "LOVE" in both names
    true_count = sum(name_1.lower().count(char) + name_2.lower().count(char) for char in "true")
    love_count = sum(name_1.lower().count(char) + name_2.lower().count(char) for char in "love")

    # Combine the counts to make a 2-digit number
    love_score = int(str(true_count) + str(love_count))

    return print(love_score)

love_score("Sherridell Knox", "Ashley McKinzie")
