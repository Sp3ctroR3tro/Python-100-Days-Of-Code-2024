ANSWER = 'N'

while ANSWER == 'n' or ANSWER == 'N':
    city = input("What's the name of the city you grew up in? \n")
    pet = input("What's you pet's name? \n")
    print(f"Your band name could be {city + ' ' + pet}")

    ANSWER = input("Does that sound like a good name? \n")

