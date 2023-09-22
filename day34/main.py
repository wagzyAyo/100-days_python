from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
from ui import QuizInterface


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Quizbrain(question_bank)
Quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#    quiz.next_question()
print("\n\nYou've completed the quiz")
print(f"Youre final score was {quiz.score}/{len(question_bank)}")
