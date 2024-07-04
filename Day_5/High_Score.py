# The following program calculates the highest score from a list without the use of the max function

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Initializing the highest score variable
max_score = 0

# Creating a for loop that will iterate over the list and place the highest score into the max score variable.
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
