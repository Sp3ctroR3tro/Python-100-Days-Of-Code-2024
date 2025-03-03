# Imports
from tkinter import *
import string
import random
from tkinter import simpledialog
from tkinter import messagebox
import json

# Function to generate a password of a specified length to the password entry field
def generate_password():
    password_length = simpledialog.askinteger("Password Length", " Min 8 characters. Enter the desired password length:", minvalue=8, maxvalue=32)
    if password_length:
        password = ""
        for i in range(password_length):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        # Copying password to clipboard using tkinter's built-in methods
        # Clear any previous clipboard content
        window.clipboard_clear()
        # Append the new password to the clipboard
        window.clipboard_append(password)
        # Ensure the clipboard content is available
        window.update()

# Function to write password information to text document
def add_password():
    # Standing user account variables
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    # Password dictionary file
    password_dictionary = {
        website:{
            "email": email,
            "password": password,
        }
    }

    # Confirm that fields are not empty
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Invalid Entry", message="Please fill in all fields.")
        return
    else:
        # Try to see if file exists and read from it
        try:
            with open("passwords.json", "r") as password_file:
                # Reading current password file
                passwords = json.load(password_file)
        # If file is not found, create the file and write to it
        except FileNotFoundError:
            # Writing data to password_file
            with open("passwords.json", "w") as password_file:
                json.dump(password_dictionary, password_file, indent=4)
        else:
            # Updating password file with new data
            passwords.update(password_dictionary)
            with open("passwords.json", "w") as password_file:
                json.dump(passwords, password_file, indent=4) # Repetition with the write file, look into making a function to make this less redundant.

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password(website):
    with open("passwords.json", "r") as password_file:
        passwords = json.load(password_file)
        try:
            website_data = passwords[website]
            email = website_data["email"]
            password = website_data["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title="Error", message="Website not found.")



# Password Manager UI
window = Tk()
window.title("Password Manager")
logo_img = PhotoImage(file="logo.png")
# Add an empty padding column (left side of the layout)
window.grid_columnconfigure(0, weight=1)
canvas = Canvas(width=1024, height=500)
canvas.create_image(514, 250, image=logo_img)
# Center the canvas (logo image)
canvas.grid(row=0, column=1, columnspan=3)

# Change column for 'website_label' to align with center
website_label = Label(text="Website:")
website_label.grid(row=2, column=1, padx=10, pady=10, sticky="E")  # Align to the right (East)

# Place the 'website_entry' right next to the label
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")  # Align to the left (West)
website_entry.focus()

# Creating a search button next to the website entry
search_button = Button(text="Search", width=12, command=lambda: search_password(website_entry.get()))
search_button.grid(row=2, column=3, padx=10, pady=10, sticky="W")
# Change column for 'Email/Username' to align with center
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1, padx=10, pady=10, sticky="E")

# Place the 'Email/Username' right next to the label
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")
email_entry.insert(0, "dizzy@gmail.com")
# Change column for 'Email/Username' to align with center
password_label = Label(text="Password:")
password_label.grid(row=4, column=1, padx=10, pady=10, sticky="E")

# Place the 'Password' right next to the label
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2, padx=10, pady=10, sticky="W")

# Placing the generate password button next to the entry
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=3, padx=10, pady=10, sticky="W")

# Placing the add button below all entry fields
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=5, column=1, columnspan=3, padx= 10, pady=10)

# Add another padding column (right side of the layout)
window.grid_columnconfigure(3, weight=1)

window.mainloop()