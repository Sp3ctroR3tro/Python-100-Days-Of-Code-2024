# The following code will prompt the user
# for a specific number of input and create a password based off of the prompts.
import random
import string

# Defining character sets
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# Combining all sets into a list
password_frame = letters + numbers + symbols

# Creating a password generation function
length = int(input("How long do you want the password to be? \n"))


def generate_password(length):
    password = ''.join(random.choice(password_frame) for i in range(length))
    return print(password)


# Calling the function
generate_password(length)
