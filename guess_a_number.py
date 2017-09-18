import random

#config
low = 1
high = 100
limit = 10

#helper function
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n)")

        if decision == 'y' or decision == 'yes':
            return True
            print("yay!")
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

again = True

while again:
    #start game
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1
    tries = 0

    while guess != rand and tries < limit:
        guess = get_guess()
        
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")
        else:
            print("You got it!")

        tries += 1
        
    if guess == rand:
        print("You win!")
    else:
        print("You suck! The number was " + str(rand) + ".")

    again = play_again()


print("Gosh you're so lame.")
