def rockpaperscissor():
    #Some initialization
    bot_win = 0
    user_win = 0
    R = "Rock"
    P = "Paper"
    S = "Scissor"
    
    while True:

        user = [R, P, S]
        bot_list = [R, P, S]
        user_input = str(input("Give your choice (Rock, Paper, Scissor): ")).capitalize()
       
        bot = random.choice(bot_list)
        #Check if the user gave a valid item
        if user_input not in user:
            bot = False
            print("Invalid choice, Choose between Rock, Paper, Scissor \n")
            continue
        else:
            print("Bot's choice is", bot)
        #Check if the bot won the round
        if bot == R and user_input == S or bot == P and user_input == R or bot == S and user_input == P:
            bot_win += 1
            print(bot, "beats", user_input)
        #Check if the user won the round
        elif bot == S and user_input == R or bot == R and user_input == P or bot == P and user_input == S:
            user_win += 1
            print(user_input, "beats", bot)
        else:
            print("It's a tie!")
        
        print("Bot points:", bot_win, "Your points:", user_win, "\n")
        #The one to get to three points wins
        if user_win == 3:
            print("\nYou win!")
            break
        elif bot_win == 3:
            print("\nYou lost!")
            break

            
            
            
            
            
            
            
            
def rockpaperscissor():
    bot_win = 0
    user_win = 0
    R = "Rock"
    P = "Paper"
    S = "Scissor"

    def check_valid_input(user_input):
        user = [R, P, S]
        if user_input not in user:
            bot = False
            print("Invalid choice, Choose between Rock, Paper, Scissor \n")
            return False
        return True

    def check_round_winner(bot, user_input):
        if bot == R and user_input == S or bot == P and user_input == R or bot == S and user_input == P:
            return "bot"
        elif bot == S and user_input == R or bot == R and user_input == P or bot == P and user_input == S:
            return "user"
        else:
            return "tie"

    while True:
        bot_list = [R, P, S]
        user_input = str(input("Give your choice (Rock, Paper, Scissor): ")).capitalize()

        if not check_valid_input(user_input):
            continue

        bot = random.choice(bot_list)
        print("Bot's choice is", bot)
        round_winner = check_round_winner(bot, user_input)
        if round_winner == "bot":
            bot_win += 1
            print(bot, "beats", user_input)
        elif round_winner == "user":
            user_win += 1
            print(user_input, "beats", bot)
        else:
            print("It's a tie!")

        print("Bot points:", bot_win, "Your points:", user_win, "\n")

        if user_win == 3:
            print("\nYou win!")
            break
        elif bot_win == 3:
            print("\nYou lost!")
            break

