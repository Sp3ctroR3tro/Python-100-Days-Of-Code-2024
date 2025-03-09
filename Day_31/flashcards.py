# Program Imports
from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
flip_timer = None
learned_words = []


# Helper Functions
def load_data():
    try:
        french_words = pd.read_csv("data/french_words.csv")
        if "French" not in french_words.columns or "English" not in french_words.columns:
            raise ValueError("CSV file must contain 'French' and 'English' columns.")
        return french_words.to_dict(orient="records")
    except Exception as e:
        print(f"Error loading data: {e}")
        return []  # Default to an empty list


# Updates the flashcard (reusable UI helper function)
def update_card(language, text, image, text_color="black"):
    canvas.itemconfig(language_title, text=language, fill=text_color)
    canvas.itemconfig(word_title, text=text, fill=text_color)
    canvas.itemconfig(canvas_image, image=image)


# Flashcard Logic 
# Handles the logic when an answer is given
def answer_check():
    global current_word, flip_timer

    # Cancel any previous flip timer
    if flip_timer:
        window.after_cancel(flip_timer)

    # Load a new word while avoiding previously learned words
    words_to_learn = [word for word in french_word_data_dictionary if word not in learned_words]
    if not words_to_learn:
        print("Congratulations! You've learned all the words!")
        window.quit()  # Exit the program if no words are left
        return
    else:
        unknown_words = pd.DataFrame(words_to_learn)
        unknown_words.to_csv("data/unknown_words.csv", index=False)

    current_word = random.choice(words_to_learn)
    french_word = current_word["French"]
    update_card(language="French", text=french_word, image=front_img, text_color="black")

    # Flip the card after 3 seconds
    flip_timer = window.after(3000, flip_card)


# Flips the flashcard to show the English translation
def flip_card():
    english_word = current_word.get("English", "Unknown")
    update_card(language="English", text=english_word, image=back_img, text_color="white")


# Marks the current word as "learned" and loads a new word
def mark_as_learned():
    learned_words.append(current_word)
    answer_check()  # Load the next word


# Data Setup 
# Load the CSV data into the dictionary
french_word_data_dictionary = load_data()
if not french_word_data_dictionary:
    print("No valid data available. Exiting the program.")
    exit()  # Exit if no valid data

# Flashcard UI Setup 
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

# Front and back card images
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# Canvas for Flashcard UI
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Text displayed on the canvas
language_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_title = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons for "Correct" and "Incorrect"
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=answer_check)
incorrect_button.grid(row=1, column=0, padx=20, pady=20)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=mark_as_learned)
correct_button.grid(row=1, column=1, padx=20, pady=20)

# Starting the App
answer_check()
window.mainloop()
