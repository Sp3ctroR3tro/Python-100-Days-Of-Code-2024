# Importing the Pandas library
import pandas as pd

# Taking our nato alphabet CSV file and turning it into a dictionary
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = nato_alphabet.set_index("letter").to_dict()["code"]

# Creating a phonetic list using the users input
word = input("Enter a word: ").upper()
for letter in word:
    print(nato_dictionary[letter], end=" ")