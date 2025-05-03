class Question:
    def __init__(self, q_text, q_answer):
        # Store the question text
        self.text = q_text
        # Store the correct answer (expected to be "True" or "False")
        self.answer = q_answer