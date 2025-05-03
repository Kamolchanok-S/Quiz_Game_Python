class QuizBrain:
    # Initialize the quiz with a list of questions
    def __init__(self, q_list = []):
        self.question_number = 0  # Track the current question number
        self.question_list = q_list  # Store the list of Question objects
        self.score = 0  # Initialize the score to 0
         
    # Check if the user's answer matches the correct answer (case-insensitive)
    def check_answer(self, answer_user, correct_answer):
        return answer_user.lower() == correct_answer.lower()
    
    # Ask the next question and process the user's answer
    def next_question(self):
        # Get the current question object from the list
        curr_q = self.question_list[self.question_number]
        # Prompt the user for an answer
        answer_user = input(f"Q.{self.question_number + 1}: {curr_q.text} (True/False): ")
        # Move to the next question
        self.question_number += 1
        # Check the user's answer and update score accordingly
        if self.check_answer(answer_user, curr_q.answer):
            self.score += 1
            print("You got it right!")
        else:
            print(f"Wrong answer! Correct answer is {curr_q.answer}")
        # Display the current score
        print(f"Your score: {self.score} / {self.question_number}\n")
        
    # Check if there are more questions left in the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    # Display the final score after the quiz ends
    def final_score(self):
        print("You've completed the quiz.")
        print(f"Your final score is : {self.score} / {len(self.question_list)}")