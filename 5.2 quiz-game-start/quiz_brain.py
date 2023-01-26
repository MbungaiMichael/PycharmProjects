class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        total_left = len(self.q_list) - self.q_number
        if total_left != 0:
            return True
        else:
            return False

    def next_question(self):
        item = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {item.text} (True / False): ").lower()
        self.check_answer(user_answer, item.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f" The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.q_number}")
        print('\n')

    def finished(self):
        print("You've completed the quiz")
        print("You're total score is ")