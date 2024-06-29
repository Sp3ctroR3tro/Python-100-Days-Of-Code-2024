weight = input("What is your weight in kg\n")
height = input("What is the height in m\n")

# Converting the input strings to floats, we could have also changed the initial variables to be of float(input()) to save a step.
float_weight = float(weight)
float_height = float(height)

# The problem wants the answer as an int, so we will change bmi to display as an int.
bmi = int(float_weight/(float_height**2))

print(bmi)