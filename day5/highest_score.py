# Highest score within a given set of numbers
student_score = input('enter a list of numbers:').split()
highest_score = 0
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
for scores in student_score:
    if scores > highest_score:
        highest_score = scores
print(highest_score)