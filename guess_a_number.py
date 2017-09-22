import random
import math

# config
low = 1
high = 100
limit = math.ceil(math.log(high-low + 1, 2))

# helper functions
def show_start_screen():
    print("""
                 $$$$$$\                                                                                                  $$\                           
                $$  __$$\                                                                                                 $$ |                          
                $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\        $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
                $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|       \____$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\         $$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\       $$  __$$ |      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
                \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |      \$$$$$$$ |      $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
                 \______/  \______/  \_______|\_______/ \_______/        \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
        """)
def show_credits():
    print(" Ugh. You're so lame. What's the point of leaving. I know you don't have a life, loser. Just kidding! Hahahaha! You're an amazing person! Thanks for playing!")
    print("This awesome game was created by " """
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |  _________   | || |   _____      | || |     _____    | || |    _______   | || |    _______   | || |      __      | |
| ||_   \  /   _|| || | |_   ___  |  | || |  |_   _|     | || |    |_   _|   | || |   /  ___  |  | || |   /  ___  |  | || |     /  \     | |
| |  |   \/   |  | || |   | |_  \_|  | || |    | |       | || |      | |     | || |  |  (__ \_|  | || |  |  (__ \_|  | || |    / /\ \    | |
| |  | |\  /| |  | || |   |  _|  _   | || |    | |   _   | || |      | |     | || |   '.___`-.   | || |   '.___`-.   | || |   / ____ \   | |
| | _| |_\/_| |_ | || |  _| |___/ |  | || |   _| |__/ |  | || |     _| |_    | || |  |`\____) |  | || |  |`\____) |  | || | _/ /    \ \_ | |
| ||_____||_____|| || | |_________|  | || |  |________|  | || |    |_____|   | || |  |_______.'  | || |  |_______.'  | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
 """)
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print(" You only have " + str(limit) + " tries.")
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You moron! The number was " + str(rand) + ". Get it right next time idiot.")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
        
def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
