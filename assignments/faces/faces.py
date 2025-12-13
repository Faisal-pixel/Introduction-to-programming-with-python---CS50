"""
Docstring for assignments.faces.faces
The replace method allows you to replace a string you specify in the first argument with 
another string you specify in the second argument. 

"""

def main():
    print(convert(input("Input a text with emoticon :) or :( and I will replace it for you with the equivalent emoji!: ")));

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁");

main();
