student_score = input("Input a list of student scores : ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
highest_score = 0
lowest_score = 10000
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}")

for score in student_score:
    if score < lowest_score:
        lowest_score = score
print(f"The highest score in the class is {lowest_score}")
