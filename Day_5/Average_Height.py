# The following program calculates the average student height from a given list of heights.
student_heights = ["151", "145", "179"]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initializing final counters
total_height = 0
total_students = 0
class_average = 0
# Creating a for loop to iterate over the numbers
for height in student_heights:
    total_height += height  # Using the height variable that contains the integer values to calculate the total class
    # height
    total_students += 1  # Adding a value of one to the total number of students each time the list iterates
    # until completion.
    class_average = total_height / total_students  # Taking the average of the class by dividing the two calculated
    # values

print(f"total height = {total_height}")
print(f"number of students = {total_students}")
print(f"average height = {class_average:.0f}")
