# Take in the users age
age = int(input("What is your current age? \n"))

# Start by finding out how many years left until the person becomes 90 years old.
years_until_90 = 90 - age

# There are 52 weeks in a year, so we would have to multiply to find the number of remaining weeks
weeks_left = years_until_90 * 52

print(f"You have {weeks_left} weeks left.")