def main():
    while True:
        try:
            x = int(input("What is x: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    print(f"x is {x}")

if __name__ == "__main__":
    main()


# can write better like this:

# def get_int():
#     while True:
#         try:
#             return f"{int(input("What is x: "))}"
#         except ValueError:
#             print("x is not an integer")
        

############### INTERESTING STUFF TO LOOK AT LATER ###############
# 1. name.split(" ", 1) if " " in name else (name, "")
# 2. if __name__ == "__main__":
#    main();