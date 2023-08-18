student_height = input("Input a list of student heights : ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
count = 0
total_height = 0
for height in student_height:
    total_height += height
    count += 1
Average_height = round(total_height / count)
print(f"Average student height is {Average_height}")
