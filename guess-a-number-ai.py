import random
import math

# Melissa V.

# config
low = 1
high = 100

print("Hello. What's your name?")
name = input()
print("Yo " + name + " can you pick a low number?")
low = input()
low = int(low)
print("Cool now pick a high number?")
high = input()
high = int(high)

# helper functions
def show_start_screen():
    print("Thanks. So...." + name + " lets play a game called...")
    print("")
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
    print("")
    print("Don't worry it's an easy game.")

def show_credits():
    print("")
    print(" Ugh. You're so lame, " + name + ". What's the point of leaving. I know you don't have a life, loser. Just kidding! Hahahaha! You're an amazing person! Thanks for playing!")
    print("")
    print("")
    print("")
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
    
def get_guess(current_low, current_high):
    """
    Returns a truncated average of the current low and high
    """
    guess = (current_low + current_high) // 2
    
    return guess 

def pick_number(limit):
    """
    Ask the player to pick a number and waits until the player
    confirms they have a number by pressing enter.
    """
    print("")
    print("Just think of a number between " + str(low) + " to " + str(high) + " and I will guess it in " + str(limit) + " tries.")
    print("")
    print("")
    input("Press Enter to continue...")
    print("")
        
    pass

def check_guess(guess):
    """
    Ask the player if the computer's number was too high, too low,
    or just right.
    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print("")
    yn = input("Is the number " + str(guess) + "? (y/n)")
    print("")
    if yn == 'y' or yn == 'yes':
        return 0
        
    elif yn == 'n' or yn == 'no':
        check = input("Was my guess too high or too low?" )

        if check == 'high' or check == 'too high' or check == 'h' :
            return 1
        elif check == 'low' or check == 'too low' or check == 'l' :
            return -1
    else:
        print("You must enter \"y\" or \"n\".")
    
def show_result(check, tries, guess):

    if check == 0:
        print("I guessed the number in " + str(tries) + " tries.")
        print("")
        print("I won! The number was " + str(guess) + "!")
        print("")
    else:
        print("")
        print("Oh shoot. I lost... or you just cheated.")
        print("")
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
    current_low = low
    current_high = high
    check = -1
    limit = math.ceil(math.log(high-low + 1, 2))
    tries = 0
    pick_number(limit)
    
    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)

        check = check_guess(guess)
            
        if check == -1:
            # adjust current high/*+
            current_low = guess +1
        elif check == 0:
            # computer guesses the correct number
            pass
        elif check == 1:
            # adjust current low
            current_high = guess -1

        tries += 1

    show_result(check, tries, guess)

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

