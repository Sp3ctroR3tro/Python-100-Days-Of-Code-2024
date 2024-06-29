weight = input("What is your weight in kg\n")
height = input("What is the height in m\n")

# Converting the input strings to floats, 
# we could have also changed the initial variables to be of float(input()) to save a step.
float_weight = float(weight)
float_height = float(height)

# The problem wants the answer as an int, so we will change bmi to display as an int.
bmi = int(float_weight / (float_height ** 2))
# print(f"{bmi:.2f}")

if bmi < 18.5:
    print(f"Your BMI is {bmi:.1f}, you are underweight")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.1f}, you have a normal weight")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.1f}, you are slightly overweight")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi:.1f}, you are obese")
else:
    print(f"Your BMI is {bmi:.1f}, you are critically obese")
