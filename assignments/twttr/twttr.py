# User passes in a word, twitter
# output twttr. Remove all the vowels
# We can have an array of vowels right... then loop over the word, if a character is in the vowels array, then we pass in an empty string

vowels = ["a", "e", "i", "o", "u"];
user_input = input("Input: ");

stripped_vowel = "";

for char in user_input:
    stripped_vowel += char if char not in vowels else ""

#or

stripped_vowel = "".join([char for char in user_input if char not in vowels])

print(f"Output: {stripped_vowel}")
# could also do it with a list comprehension
# stripped_vowel = ''.join([char for char in user_input if char not in vowels])
# could also do it with a list comprehension
# stripped_vowel = ''.join([char for char in user_input if char not in vowels])

