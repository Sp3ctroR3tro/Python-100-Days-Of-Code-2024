# The main goal of this program is to determine if a particular
# year is a leap year.

year = int(input("Enter the year in question \n"))


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


leap_year(year)
