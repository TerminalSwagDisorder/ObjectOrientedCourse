# File name: Exercise2_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing all the code for excercise 2 of OOP course

#Calculate student grade
def student_grade():
    student = input("Enter student name: ")
    points = int(input("Enter student points (0-120): "))
    presence = int(input("Enter student presence (0-100): "))

    if presence < 75:
        points = int(points * 0.9)

    if points < 60:
        grade = 0
    else:
        grade = (points // 12) - 4
        if grade > 5:
            grade = 5    

    if points < 0 or points > 120:
        print("\nPoints cannot be outside the range of 0-120")
    elif presence < 0 or presence > 100:
        print("\nPresence cannot be outside the range of 0-100")
    else:
        print("\nStudent:", student)
        print("Grade", grade)

student_grade()