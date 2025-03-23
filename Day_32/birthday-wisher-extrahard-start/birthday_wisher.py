
# Program Imports
import smtplib
import datetime as dt
import random
import pandas as pd
import os

# email user creds
user_email = # User email here
user_password = # User password here


# Defining Program Helper Functions
# Explicitly defining the birthday.csv to read
def check_birthdays(file_name="birthdays.csv"):
    # Checking to see if the file exists
    try:
        birthday_list = pd.read_csv(file_name)
        return birthday_list
    except FileNotFoundError:
        print("The birthdays file was not found. Please check the file name and try again.")

def match_birthday(birthday_list):
    # Loading the current date
    today = dt.datetime.now()
    # Initializing the birthday person and email lists
    birthday_people = []
    birthday_email_list = []
    # Iterating through the birthday dataframe
    for index, row in birthday_list.iterrows():
        # Returning the name and email series if the current date is the same as the value within the month and day series
        if today.month == row.month and today.day == row.day:
            birthday_people.append(row["name"])
            birthday_email_list.append(row["email"])
    return birthday_people, birthday_email_list


def generate_letter(birthday_people):

    # Initializing outfile information
    personal_letter_details = []

    # Checking to see if there is an outfile directory and if not creating one
    if not os.path.exists("Personal_Letters"):
        os.makedirs("Personal_Letters")

    # Iterating through the birthday name list

    # Create personalized letters
    for name in birthday_people:
        try:
            # Choose a random letter template
            random_letter = random.randint(1, 3)

            # Read the chosen letter template's content
            with open(f"letter_templates/letter_{random_letter}.txt", "r") as letter_file:
                letter_contents = letter_file.read()

            # Replace placeholder [NAME] with the person's actual name
            personal_letter = letter_contents.replace("[NAME]", name)

            # Write letter to a file
            output_path = os.path.join("Personal_Letters", f"{name}.txt")
            with open(output_path, "w") as birthday_letter:
                birthday_letter.write(personal_letter)

            # Append name, email, and letter file path to details list
            personal_letter_details.append((name, output_path))

        except FileNotFoundError:
            print(f"The letter template for {name} was not found.")
        except Exception as e:
            print(f"An error occurred while generating the letter for {name}: {e}")
    return personal_letter_details


def send_email(email_list, letter_details):
    if not email_list or not letter_details:
        print("No emails to send. Either email list or letter details are empty.")
        return

    try:
        # Establish SMTP connection
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user_email, password=user_password)

            # Send each email
            for (name, email), (_, letter_path) in zip(email_list, letter_details):
                try:
                    # Read the content of the personalized letter
                    with open(letter_path, "r") as letter_file:
                        letter_content = letter_file.read()

                    # Send email
                    connection.sendmail(
                        from_addr=user_email,
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday!\n\n{letter_content}"
                    )
                    print(f"Email successfully sent to {email}.")
                except Exception as e:
                    print(f"Failed to send email to {email}. Error: {e}")
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication failed. Check your email credentials or App Password.")
    except TimeoutError:
        print("Connection timed out. Please check your network or SMTP configuration.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Main Program Logic
if __name__ == "__main__":
    # Step 1: Load birthdays
    birthday_list = check_birthdays()

    # Step 2: Match today's birthdays
    birthday_people, birthday_email_list = match_birthday(birthday_list)

    if not birthday_people:
        print("No birthdays today!")
    else:
        # Step 3: Generate letters
        letter_details = generate_letter(birthday_people)

        # Print confirmation of letters generated
        for name, letter_path in letter_details:
            print(f"Generated letter for {name}: {letter_path}")

        # Step 4: Send emails
        send_email(zip(birthday_people, birthday_email_list), letter_details)
