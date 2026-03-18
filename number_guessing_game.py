import random

# computer ek number choose karega
num = random.randint(1, 100)

guess = 0
attempts = 0

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while guess != num:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > num:
        print("Too large")
    elif guess < num:
        print("Too small")
    else:
        print("Correct!")
        print("Total attempts:", attempts)
