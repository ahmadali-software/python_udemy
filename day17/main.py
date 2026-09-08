from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    q = Question(q_text= question["text"], q_answer= question["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print(f"your final score is {quiz.score}/{len(quiz.questions_list)}")