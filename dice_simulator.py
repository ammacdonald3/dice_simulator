# Import random function
import random as rand


# Define function - roll
def roll():
    # Ask user how many sides should be on the die
    roll_num = input("How many digits do you want on your die? ")
    # Ask user for their guess
    user_selection = int(
        input("What number do you think that it will land on? "))
    # Randomly pick a number based on the size of the die
    random_selection = rand.randint(1, int(roll_num))
    # Check if user selection equals the random selection
    if user_selection == random_selection:
        # Tell the user that they guessed correctly
        print(
            (f"Your dice had {roll_num} sides. You correctly guessed that it"
             f" would land on {user_selection}. Great job!"))
    else:
        # Tell the user that they guessed incorrectly
        print(f"Your dice had {roll_num} sides. You guessed {user_selection}"
              f" but it landed on {random_selection}. Better luck next time!")


# Set the loop
while True:
    # Call the roll() function
    roll()
    # After function is returned, ask whether to keep playing
    again = input("Do you want to keep playing? (y/n) ")
    # Check whether the user input a valid value
    if again not in ['y', 'n', 'yes', 'no']:
        print("You did not enter a valid value!")
    # If user chose not to continue, break the loop
    elif again == 'n':
        break
