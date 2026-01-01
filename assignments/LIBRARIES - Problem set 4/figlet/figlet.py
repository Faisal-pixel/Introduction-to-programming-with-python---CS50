# I will need to import sys and use sys.argv to get the command line input with the first index , 0, being the name of the file...

# if len(sys.argv) == 0, then using random.randint(0, len of total list of supported fonts), print out a randomg font text

# Then check if len(sys.argv) == 2

# Then now we are sure the argument is exactly 2, if sys.argv[1] !== "-f" or it is not equal to "--font", then exit it

# then install pyfiglet and use the getFonts() method to get the list of fonts supported

# then check if sys.argv[2] is in the list of fonts supported, if it is not... then exit the program saying "Font is not supported"

#

import random
import sys
from pyfiglet import Figlet

def main():

    figlet = Figlet()

    supported_font_list = figlet.getFonts()
    # print("Supported Font List:", *supported_font_list, sep="\n")

    if len(sys.argv) == 1:
        index_of_random_font = random.randint(0, len(supported_font_list))
        font_name = supported_font_list[index_of_random_font]
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font": # Read a about this and the pythonic way on here: https://chatgpt.com/g/g-p-69283b7352048191bd487312008c1cca/c/69570409-a650-8330-aadd-1cf3bb85ed2e
            print("This is the first command line argument", sys.argv[1], "It's type is: ", type(sys.argv[1]), sys.argv[1] != "-font")
            sys.exit("First command line argument must be -f or --font")

        if sys.argv[2] in supported_font_list:
            font_name = sys.argv[2]
        else:
            sys.exit("Font is not supported!")
    else:
        sys.exit("Too few inputs or too many inputs")

    user_input = input("Input: ")
    figlet.setFont(font=font_name)
    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()

