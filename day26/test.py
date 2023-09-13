import random
names = {"Alex", "Beth", "Eleanor", "james", "Dave", "Caroline", "Freddie"}

student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

passed_student = {student: score for (student, score)
                  in student_score.items() if score >= 60}
print(passed_student)
