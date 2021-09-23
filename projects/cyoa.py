"""A choose your own adventure program!"""
__author__ = "730490857"

from random import randint
points: int = 0
total_points: int = 0
player: str = ""
SMILEY_FACE: str = "\U0001F604"
x: int = 0
i: int = 0


def main() -> None: 
    """Main function."""
    global points
    global i
    while i < 1:
        greet()
        i = i + 1
    print("1 = Coin Flip Chaos!")
    print("2 = Guess That Number!")
    print("3 = Fortune Cookie Store")
    print("4 = Exit")
    choice = int(input("Where would you like to go? "))
    if choice == 1:
        coin_flip_chaos()
    elif choice == 2:
        x: int = int(input("What number would you like to guess (between 1 and 10)? "))
        print(f"You've accumulated {guess_that_number(x)} points!")
        print(f"You now have {points} points!")
        print("Back to the start.")
        main()
    elif choice == 3:
        points = fortune_cookie_store(points)
        print(f"You now have {points} point(s) {player}!")
        print("Back to the start.")
        main()
    elif choice == 4:
        return


def greet() -> None:
    """Greeting to player."""
    print(f"Greetings! Welcome to Random Town USA!{SMILEY_FACE}")
    global player
    player = str(input("What is your name? "))
    print(f"{player}! We are so glad you could make it to our town of fun and games and fortunes! Play games to accumulate points and spend them on fortunes!")
    print("We used to have a lot of games but we are now down to only two...")
    print("Don't forget to check out our fortune shop with the points you accumuate!")
    return


def coin_flip_chaos() -> None:
    """A fun guessing game with coin flips."""
    play_game: int = int(input("Welcome to Coin Flip Chaos " + player + "!" + SMILEY_FACE + " Would you like to flip a coin? (1 = Yes, 2 = No) "))
    global points
    global total_points
    if play_game != 1 and play_game != 2:
        print("That wasn't a 1 or a 2 silly, try again.")
        coin_flip_chaos()
    else:
        if play_game == 1:
            i: int = 0
            print("You get 5 tries to get a maximum of 5 points!")
            while i < 5:
                heads_or_tails: int = randint(1, 2)
                answer: int = int(input("Flipping your coin... heads or tails? (1 = Heads, 2 = Tails) "))
                if heads_or_tails == answer:
                    print("Good job you got it right! Go again!" + "\U00002705")
                    points = points + 1
                    total_points = total_points + 1
                    i = i + 1
                else:
                    print("Oh no, you got it wrong! Try again!" + "\U0000274C")
                    i = i + 1
            print(f"You now have {points} point(s) {player}!")
            print("Back to the start.")
            main()
        else:
            print(f"Thanks for stopping by {player}!")
            main()


def guess_that_number(x: int) -> int:
    """Guessing game that increases points by the amount of the radom number generated once the player guesses the random number."""
    global points
    global total_points
    random_number: int = randint(1, 10)
    while x != random_number:
        if x > random_number:
            print(player + " You guessed too high!" + "\U00002B07")
        else:
            print(player + " You guessed too low!" + "\U00002B06")
        x = int(input("Guess again "))
    points = points + random_number
    total_points = total_points + random_number
    return random_number


def fortune_cookie_store(points: int) -> int:
    """Function that allows player to spend points they earned on 1 out of 10 random fortune cookies."""
    print("Welcome to the fortune cookie store!" + "\U0001F960")
    answer: str = str(input("Would you like a fortune cookie? (Yes or No) "))
    if answer == "Yes":
        fortune: int = randint(1, 10)
        if points < 5:
            print(f"Sorry {player} you do not have enough have enough points. Go play some games and get some more!" + SMILEY_FACE)
            main()
        else:
            if fortune == 1:
                print("A mysterious travler will brighten your day next week." + "\U0001F31E")
            elif fortune == 2:
                print("You will come across a very cute puppy." + "\U0001F436")
            elif fortune == 3:
                print("You will fall in a hole... of butterflies." + "\U0001F98B")
            elif fortune == 4:
                print("You will wake up as a magnificent dancer." + "\U0001F483")
            elif fortune == 5:
                print("You will one day own Random Town USA." + SMILEY_FACE)
            elif fortune == 6:
                print("You will find out you are adopted." + "\U0001F476")
            elif fortune == 7:
                print("You will get another fortune cookie." + "\U0001F960")
            elif fortune == 8:
                print("A leaf will land on your head, and you will be happy." + "\U0001F343")
            elif fortune == 9:
                print("You will be adopted by an elephant?" + "\U0001F418")
            elif fortune == 10:
                print("A hundred bucks will fly into your hands." + "\U0001F4B8")
        points = points - 5
        return points
    else:
        print("Back to the start.")
        return points


if __name__ == "__main__":
    main()

print(f"{player}, thankyou so much for playing here in Random Town USA!")
print(f"You have accumalted {total_points} total point(s) during your experience here and ended with {points} point(s)!")
print(f"Please come again!{SMILEY_FACE}")