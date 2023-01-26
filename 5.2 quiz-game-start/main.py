from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain


q_bank = []
for question in question_data:
    q_text = (question['text'])
    q_answer = (question['answer'])
    new_q = Questions(q_text, q_answer)
    q_bank.append(new_q)

quiz = QuizBrain(q_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"You're total score is {quiz.score}/{quiz.q_number}")
