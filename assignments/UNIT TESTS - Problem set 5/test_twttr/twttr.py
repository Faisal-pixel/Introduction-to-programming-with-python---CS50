# User passes in a word, twitter
# output twttr. Remove all the vowels
# We can have an array of vowels right... then loop over the word, if a character is in the vowels array, then we pass in an empty string

# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# user_input = input("Input: ")

# stripped_vowel = ""

# for char in user_input:
#     stripped_vowel += char if char not in vowels else ""

# print(f"Output: {stripped_vowel}")

################################# FOR UNIT TEST - PROBLEM SET - 5 ############################################

def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

def shorten(word):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    stripped_word = ""
    for char in word:
        stripped_word += char if char not in vowels else ""
    return stripped_word

if __name__ == "__main__":
    main()


################################# FOR UNIT TEST - PROBLEM SET - 5 ############################################