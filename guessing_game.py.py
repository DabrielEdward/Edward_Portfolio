import random

print("Welcome to the Number Guessing Game!")

# Step 1: 
secret_number = random.randint(1, 20)

# Step 2: 
guess = int(input("Guess a number between 1 and 20: "))
attempts = 1

# Step 3: 
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    guess = int(input("Guess again: "))
guess = int(input("Guess again: "))
attempts += 1

print("Yabba Dabba Doo! The number was", secret_number)
