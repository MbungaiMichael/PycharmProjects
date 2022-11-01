#getting the average height of students
student_height = input('enter the heights of the students: ').split()
a = 0
b = 0
for n in range(0, len(student_height)):
    student_height[n]= int(student_height[n])
    a += student_height[n]
    b +=1
print(f'The average is {round(a/b)}')