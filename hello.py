def hello():
    print("Hello")

name = input("What's your name? ").strip().title();

first, last = name.split(" ");

print(f"Hello, {first} {last}!");



############### INTERESTING STUFF TO LOOK AT LATER ###############
# 1. name.split(" ", 1) if " " in name else (name, "")
# 2. if __name__ == "__main__":
#    main();