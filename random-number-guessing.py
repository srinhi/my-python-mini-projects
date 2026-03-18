import random

def get_valid_guess():
    guess = input("Guess a number between 1 and 100: ")
    while (not guess.isdigit()) or (int(guess) > 100 or int(guess) < 1):
        guess = input("Invalid input. Please enter a number between 1 and 100: ")
    return int(guess)
    

while True:
    random_integer = random.randint(1, 100)
    guess = get_valid_guess()
    guess_counter = 1

    while(guess != random_integer):
        if(guess > random_integer):
            print("Too high! Try again.")
            guess = get_valid_guess()
        elif(guess < random_integer):
            print("Too low! Try again.")
            guess = get_valid_guess()
        guess_counter = guess_counter + 1

    print(f"Congratulations! You guessed the number! It only took {guess_counter} guesses.")
    play_again = input("Do you want to play again? (yes/no): ")

    while play_again != "yes" and play_again != "no":
        play_again = input("Invalid input. Please enter yes or no: ")
    
    if(play_again == "no"):
        break

print("Thank you for playing!")