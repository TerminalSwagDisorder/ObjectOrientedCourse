# File name: Exercise2_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing all the code for excercise 2 of OOP course

import random
import datetime
import time

# Calculate student grade
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

# Calculate average grade of multiple students
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

# Class for alarm clock
class AlarmClock2:
    def __init__(self):
        self.current_time = datetime.datetime.now().strftime("%X")
        self.alarm_time = None
        self.alarm_active = False
        self.alarm_sound = None
        self.snooze_duration = datetime.timedelta(minutes=10)

    def set_alarm(self, time: datetime.datetime):
        if time.strftime("%X") > self.current_time:
            self.alarm_time = time.strftime("%X")
        else:
            raise ValueError("Alarm time must be in the future")

    def snooze_alarm(self):
        self.alarm_time += self.snooze_duration

    def turn_off_alarm(self):
        self.alarm_active = False

    def _play_alarm_sound(self):
        print("Playing alarm sound:", self.alarm_sound)

    def _check_alarm(self):
        self.current_time = datetime.datetime.now().strftime("%X")
        if str(self.current_time) == str(self.alarm_time) and self.alarm_active:
            print("Time's up")
            self._play_alarm_sound()
            
def run_alarm_clock():
    alarm = AlarmClock2()
    
    print("Current time:", alarm.current_time)
    alarm_time_input = str(input("Enter the alarm time (HH:MM:SS): "))
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_input, "%H:%M:%S")
    except ValueError:
        print("Incorrect time format, use (HH:MM:SS)")
        return

    alarm.set_alarm(datetime.datetime.now() + datetime.timedelta(seconds=10))
    alarm.alarm_sound = "alarm.mp3"
    alarm.alarm_active = True
    
    while True:
        alarm._check_alarm()
        time.sleep(1)
        if False:
            break
        
#student_grade()
#avg_grade()
#coin()
run_alarm_clock()
