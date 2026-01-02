import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            print("") # Doing this because the EOFError doesnt take you to the next line, but instead remain on the same line, so because print has and end line set to new line, we get pushed to the nex tline
            break
    print(f"Adieu, adieu, to {p.join(names)}")

main()
