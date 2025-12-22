"""
Docstring for assignments.camel.camel
 So what did i learn here!
 1. Learnt that it is possible to iterate over a string character by character.
 2. Learnt about the isupper() method to check if a character is uppercase.
 

"""

def main():
    user_input = input("camelCase: ")
    snake_case = convert_to_snake_case(user_input)
    print(snake_case)

def convert_to_snake_case(user_input):
    new_string = ""
    for char in user_input:
        new_string += f"_{char.lower()}" if char.isupper() else char
    return new_string

main()
