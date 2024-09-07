age = int(input("What is your age? \n"))
def life_in_weeks(age):
    age_in_weeks = age * 52
    weeks_until_90 = 90 * 52

    weeks = weeks_until_90 - age_in_weeks

    print(f"You have {weeks} weeks left.")


life_in_weeks(age)