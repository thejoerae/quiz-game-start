# TODO 1: ask the question
# TODO 2: checking if the answer was correct
# TODO 3: check if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.question_score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got that right.")
            self.question_score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.question_score}/{self.question_number}")
        print("\n")





