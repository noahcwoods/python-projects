from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    question_bank.append(Question(dict['question'], dict['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou have completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")