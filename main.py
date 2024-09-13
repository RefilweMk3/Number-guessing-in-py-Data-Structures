import random

def number_guessing_game():
    lowB = 1
    upB = 100

    secretN = random.randint(lowB, upB)
    guesses = []
    print(f"Guess the number between {lowB} and {upB}!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < lowB or guess > upB:
                print(f"Your guess must be between {lowB} and {upB}!")
                continue

            guesses.append(guess)

            if guess < secretN:
                print("Too low!")
            elif guess > secretN:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secretN} correctly.")
                print(f"It took you {len(guesses)} guesses.")
                print(f"Your guesses were: {guesses}")
                break
        
        except ValueError:
            print("Please enter a valid number.")
number_guessing_game()