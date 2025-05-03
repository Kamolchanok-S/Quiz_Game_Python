# Import the Question class, the list of questions, and the QuizBrain logic
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list to store Question objects
question_bank = []
for q in question_data:
    # Convert each dictionary in question_data to a Question object
    question_bank.append(Question(q["text"], q["answer"]))

# Initialize the quiz engine with the list of questions
quiz = QuizBrain(question_bank)

# Continue asking questions while there are still unanswered ones
while quiz.still_has_questions():
    quiz.next_question()

# Print the final result after all questions have been answered
quiz.final_score()