from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

# Creating a blank list for the bank of questions.
question_bank = []

# Creating a for loop to create a question and answer variable and assign them to our Questions class
for info in question_data:
    question, answer = info.values()
    q = Questions(question, answer)
    # Appending the question object to the question bank
    question_bank.append(q)

# Initializing the quiz object, and creating a loop to run the program
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


