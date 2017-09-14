import random

#config
low = 1
high = 100
limit = 10

rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
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
