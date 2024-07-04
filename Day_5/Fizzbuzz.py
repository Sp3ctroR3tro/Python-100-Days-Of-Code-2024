# The following program is the FizzBuzz game.
# If a number is divisible by 3 it will be replaced with "Fizz".
# If a number is divisible by 5 it will be replaced with "Buzz".
# If a number is divisible by both 5 and 3 it will be replaced with "FizzBuzz".


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)