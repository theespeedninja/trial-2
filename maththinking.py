#Ask the use to input a score
score = int(input("Enter the student's score(0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B' 
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The student's grade is: {grade}")  # Display the grade based on the score