# File name: Exercise2_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing all the code for excercise 2 of OOP course

import random

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

#Calculate average grade of multiple students
def avg_grade():
    grades = {}
    all_grades = []

    while True:
        try:
            student = input("Enter student name: ")
            grade = int(input("Enter student grade (0-5): "))
        except ValueError:
            grade = None
        try:
            if grade is None or grade == None or student == "":
                print("\nYou must input something to both fields")
            elif grade < 0 or grade > 5:
                print("\nGrade cannot be outside the range of 0-5")
            else:
                if student in grades:
                    grades[student].append(grade)
                    all_grades.append(grade)
                else:
                    grades[student] = [grade]
                    all_grades.append(grade)

            end_loop = input("Enter 'y' to continue or 'n' to end: ").capitalize()
            if end_loop == "N":
                break
            elif end_loop =="Y":
                continue
            else:
                print("\nOnly allowed inputs are 'y' or 'n'")
        except UnboundLocalError:
            break
    if len(grades) != 0 or len(all_grades) != 0:          
        for student, grades in grades.items():
            average_grade = int(sum(grades) / len(grades))
            print("\nStudent:", student)
            print("Average grade:", average_grade)
        all_average_grade = int(sum(all_grades) / len(all_grades))
        print("\nAverage grade of all students:", all_average_grade)

# Class for coins
class Coin:
    def __init__(self):
        self.sideup = "Heads"
        
    def toss(self):
        rng = random.randint(0, 11)
        if 0 <= rng <= 4:
            self.sideup = "Heads"
        elif rng == 10:
            self.sideup = "Side"
        elif rng == 11:
            self.sideup = "Coin dissappears"
        else:
            self.sideup = "Tails"
            
    def get_sideup(self):
        return self.sideup

    
# Function for displaying the coin

def coin():

    my_coin = Coin()
    strangers_coin = Coin()
    
    i = 0
    while i < 10:
        i += 1
        print("\nState of my coin:")
        print(my_coin.get_sideup())

        my_coin.toss()

        print("New state of my coin:")
        print(my_coin.get_sideup())


student_grade()
avg_grade()
coin()