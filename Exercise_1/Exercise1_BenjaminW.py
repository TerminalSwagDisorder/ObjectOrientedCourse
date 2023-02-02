# File name: Exercise1_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing all the code for excercise 1 of OOP course

import random


# Print out hello
def hello():
    print("Hello")

# Print out list of integers
def numlist():
    nlist = [2, -5, 4, 7, 9, 11, 0, 445, -100, 4]
    print("Integers:", nlist)

# Print out list of strings
def strlist():
    slist = [" abc ", "34re5", " word ", " qwerty ", " cat-doc ", " def ", "4", "# -!?bc ", " alkf ", " oooooo "]
    print("Strings:", slist)

# Sort a list of integers an print them
def sortednums():
    sortlist = [2, -5, 4, 7, 9, 11, 0, 445, -100, 4]
    print("Arranged list:", sorted(sortlist))

# Make the user input numbers, and print the number of negative numbers, and break when 0 
def intneg():
    negnumbers = []
    while True:
        try:
            number = int(input("Please give an integer (0 (zero) ends the input): "))
            if number == 0:
                break
            elif number > 0:
                continue
            elif number < 0:
                negnumbers.append(number)
        except ValueError:
            print("Please only use positive and negative integers!")
            continue
    print("\nNumber of negative integers is:", len(negnumbers))

# Make the user input numbers, and print the number of even numbers, and break when 0 
def inteven():
    evennumbers = []
    while True:
        try:
            number = int(input("Please give an integer (0 (zero) ends the input): "))
            if number == 0:
                break
            elif (number % 2) != 0:
                continue
            elif (number % 2) == 0:
                evennumbers.append(number)
        except ValueError:
            print("Please only use positive and negative integers!")
    print("\nNumber of even integers is:", len(evennumbers))

# Make the user input numbers, and print the sum of numbers that are positive and divisible by three, and break when 0 
def intthree():
    threenumbers = []
    while True:
        try:
            number = int(input("Please give an integer (0 (zero) ends the input): "))
            if number == 0:
                break
            elif number < 0:
                continue
            elif (number % 3) == 0 and number > 0:
                threenumbers.append(number)
        except ValueError:
            print("Please only use positive and negative integers!")
    print("\nSum of integers divisible by three:", sum(threenumbers))

# Arithmetic procession
def ap_terms(a, d, max_val):
        if max_val < 3:
            return 0
        terms = [a]
        while terms[-1] + d <= max_val:
            terms.append(terms[-1] + d)
        return terms

#Arithmetic procession start
# Return the progression of the AP
def ap_progression(a, d, max_val):
        terms = ap_terms(a, d, max_val)
        if not terms:
            return "Procession is: "
        return "Procession is: " + ", ".join([str(term) for term in terms])

# Return number of terms in the AP
def term_amount(terms):
        if not terms:
            return 0
        return len(terms)

# Return the sum of the terms of the AP
def term_sum(terms):
        if not terms:
            return 0
        return sum(terms)

# Return the sum of the squared terms of the AP 
def term_squared_sum(terms):
        if not terms:
            return 0
        return sum([i**2 for i in terms])
    
def arithmetic_procession():
    a = 3
    d = 3
    while True:
        try:
            max_val = int(input("Enter the maximum value:"))
            terms = ap_terms(a, d, max_val)
            print(ap_progression(a, d, max_val))
            print("Number of terms:", term_amount(terms))
            print("Sum of terms:", term_sum(terms))
            print("Sum of squared terms:", term_squared_sum(terms))
            break
        except ValueError:
            print("Please only use positive and negative integers!")

# Rock paper and scissors game
def rockpaperscissor():
    
    bot_win = 0
    user_win = 0
    R = "Rock"
    P = "Paper"
    S = "Scissor"
    choices = [R, P, S]
    
    def check_valid_choice(user_input, choices):
        if user_input not in choices:
            print("Invalid choice, Choose between Rock, Paper, Scissor \n")
            return False
        return True

    def check_winner(bot, user_input):
        if bot == R and user_input == S or bot == P and user_input == R or bot == S and user_input == P:
            print(bot, "beats", user_input)
            return "bot"
        elif bot == S and user_input == R or bot == R and user_input == P or bot == P and user_input == S:
            print(user_input, "beats", bot)
            return "user"
        else:
            print("It's a tie!")
            return "tie"
    
    while True:
        user_input = str(input("Give your choice (Rock, Paper, Scissor): ")).capitalize()
        if not check_valid_choice(user_input, choices):
            continue
        
        bot = random.choice(choices)
        print("Bot's choice is", bot)
        
        result = check_winner(bot, user_input)
        if result == "bot":
            bot_win += 1
        elif result == "user":
            user_win += 1
        
        print("Bot points:", bot_win, "Your points:", user_win, "\n")
        if user_win == 3:
            print("\nYou win!")
            break
        elif bot_win == 3:
            print("\nYou lost!")
            break

# Random number
def intrand():
    num = random.randint(1, 6)
    return num


hello()
numlist()
strlist()
sortednums()
intneg()
inteven()
intthree()
arithmetic_procession()
rockpaperscissor()
print("Random number is:", intrand())
