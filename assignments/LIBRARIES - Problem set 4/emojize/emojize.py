# so install the emojize library

# then import it

# as the user the string

# then get the index of the first : in the inputed string

# then slice the string

from emoji import emojize

def main():
    user_input = input("Input: ")

    colon_index = user_input.index(":")

    emoji_code = user_input[colon_index:]

    output_text = emojize(f"{user_input[:colon_index]}{emoji_code}", language='alias')

    print(output_text)

if __name__ == "__main__":
    main()
