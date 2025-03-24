import random

print("I've chosen a random number between 1 and 100.")
print("Can you guess it?")

target = random.randint(1, 100)
success = False

for guesses in range(10):
    print(f"You have {10 - guesses} guesses left.")
    guess_str = input("Make a guess: ")

    try:
        guess = int(guess_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if guess < target:
        print("Oops. Your guess was LOW.")
    elif guess > target:
        print("Oops. Your guess was HIGH.")
    else:
        print("Good job! You guessed it!")
        success = True
        break

if not success:
    print(f"Sorry, you didn't guess my number. It was: {target}")