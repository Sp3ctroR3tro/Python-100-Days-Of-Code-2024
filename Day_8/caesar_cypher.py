alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import caesar_logo
from caesar_logo import logo
print(logo)



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def decrypt(cipher_text, shift_amount):
   original_text = ""
   for letter in cipher_text:
       if letter in alphabet:
           new_position = (alphabet.index(letter) - shift_amount) % 26
           original_text += alphabet[new_position]
       else:
           original_text += letter
   return original_text



def caesar(original_text, shift_amount, cipher_type):
    if cipher_type == "encode":
        return encrypt(original_text, shift_amount)
    elif cipher_type == "decode":
        return decrypt(original_text, shift_amount)
    else:
         print("incorrect input")

while True:
    user_input = input("Would you like to encode or decode a message? Type 'exit' to quit.\n").lower()
    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif user_input not in ["encode", "decode"]:
        print("Invalid input. Please type 'encode' or 'decode' or 'exit' to quit.")
        continue

    original_text = input("What is the message:\n").lower()
    shift_amount = int(input("What is the shift amount:\n"))
    result = caesar(original_text=original_text, shift_amount=shift_amount, cipher_type=user_input)
    print(result)