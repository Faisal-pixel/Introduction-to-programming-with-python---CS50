import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                raise ValueError("Number must be positive")
        except ValueError:
            pass
        else:
            break

    random_no = random.randint(1, n)
    while True:
        try:
            guessed_no = int(input("Guess: "))
            if guessed_no <= 0:
                raise ValueError("Guessed Number must be positive")
        except ValueError:
            pass
        else:
            if guessed_no < random_no:
                print("Too small!")
            elif guessed_no > random_no:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()


main();
