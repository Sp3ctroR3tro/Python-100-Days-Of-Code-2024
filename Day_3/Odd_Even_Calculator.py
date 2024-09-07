# Input section
number = int(input("What is the value we are testing?\n"))

# logic loop to see if the input is an odd or even number
if number % 2 == 0:
    print("The number is even")
elif number % 2 != 0:
    print("The number is odd")
else:
    print(ValueError)

print(2000 % 4)